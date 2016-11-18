class HT:
    def __init__(self):
        self._A=[ None for i in range(10)]
        self._B=[ None for i in range(10)]
        self._size=0

    def __getitem__(self,key):
        h1=hash((key,0))%len(self._A)
        h2=hash((key,1))%len(self._B)
        if self._A[h1]!=None:
            if self._A[h1][0]==key:
                return self._A[h1][1]
        if self._B[h2]!=None:        
            if self._B[h2][0]==key:
                return self._B[h2][1]
        else:
            return None

    def __setitem__(self,k,v):
        self.insert(k,v)
    def __delitem__(self,key):
        #print(len(self.keys()))
        #print(key)
        h1=hash((key,0))%len(self._A)
        h2=hash((key,1))%len(self._B)
        if self._A[h1]:
            if self._A[h1][0]==key:
                self._A[h1]=None
                self._size-=1
        if self._B[h2]:
            if self._B[h2][0]==key:
                self._B[h2]=None
                self._size-=1
        k=self.keys()
        #print(k)


    def __len__(self):
        return self._size
    def __contains__(self,key):
        return self.__getitem__(key)!=None
    def __iter__(self):
        print("iter")
        for a in self._A:
            if a:
                yield a
        print("b")
        for b in self._B:
            if b:
                yield b

    def keys(self):
        return [i[0] for i in self._A if i]+[j[0] for j in self._B if j]
    def values(self):
        return [i[1] for i in self._A if i]+[j[1] for j in self._B if j]
    def items(self):
        return [(i[0],i[1]) for i in self._A if i]+[(j[0],j[1]) for j in self._B if j]

    def insert(self,k,v):   
        first=hash((k,0))%len(self._A)

        def insertA(k,v,f=True): 
            h=hash((k,0))%len(self._A)
            #print(k)
            if f:
                if first==h:
                    self._resize(2* len(self._A))
                    self.insert(k,v)
                    return

            
            if self._A[h]!=None:
                
                if self._A[h][0]==k:
                    self._A[h]=(k,v)
                
                else:
                    x=self._A[h]
                    self._A[h]=(k,v)
                    insertB(x[0],x[1])
                    self._size+=1
            else:
                self._A[h]=(k,v)
            self._size+=1

            if self._size > 2* len(self._A):
                 self._resize(2* len(self._A))


        def insertB(k,v):
            h=hash((k,1))%len(self._B)
            
            if self._B[h]!=None:
                if self._B[h][0]==k:
                    self._B[h]=(k,v)

                else:
                    x=self._B[h]
                    self._B[h]=(k,v)
                    insertA(x[0],x[1])
                    self._size+=1
            else:
                self._B[h]=(k,v)
            self._size+=1

            if self._size > 2* len(self._A):
                self._resize(2* len(self._A))

        insertA(k,v,False)

    def _resize(self,newsize):
        #print("resize")
        data=self.items()
        self._A=[None for i in range(newsize)]
        self._B=[None for i in range(newsize)]
        self._size=0

        for tup in data:
            #print(tup)
            self.insert(tup[0],tup[1])

        
T=HT()
for i in range(400):
    T[i]=i*i
##changes value
tmp=sorted(T.keys())

for i in tmp:
    tmpNum=T[i]
    T[i]=T[i]+1
    if(tmpNum==T[i]):
        print(T[i])


for i in range(5,400):
    if i in T:
        del T[i]
K=T.items()
K.sort()
print(K)
print(len(K))

