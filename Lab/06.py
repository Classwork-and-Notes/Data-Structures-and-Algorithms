
#---------------The PList code I posted earlier---------

class PList:
    class _Node:
        def __init__(self,data,prev,next,dir):
            self._data=data
            self._dir=dir
            self._a=prev
            self._b=next
        def prev(self):
            if self._dir._forward:
                return self._a
            else:
                return self._b
        def next(self):
            if self._dir._forward:
                return self._b
            else:
                return self._a
        def cprev(self, a):
            if self._dir._forward:
                self._a=a
            else:
                self._b=a
        def cnext(self,a):
            if self._dir._forward:
                self._b=a
            else:
                self._a=a

    class Position:
        def __init__(self,plist,node):
            self._plist=plist
            self._node=node
            self._valid=plist._valid
        def data(self):
            return self._node._data
        def __eq__(self,other):
            return type(other) is type(self) and other._node is self._node
        def __ne__(self,other):
            return not (self == other)
    class valid:
        def __init__(self):
            self._good=True
        def invalid(self):
            self._good=False
    def _validate(self,p):
        if not isinstance(p,self.Position):
            raise TypeError("p must be proper Position type")
        if p._plist is not self:
            raise ValueError('p does not belong to this PList')
        if p._node is None:
            raise ValueError('p is no longer valid')
        if not p._valid._good:
            raise ValueError('pls work')
        if p._valid._good != self._valid._good:
            raise ValueError('pls work')

        return p._node
    def _make_position(self,node):
        if node is self._head or node is self._tail:
            return None
        else:
            return self.Position(self,node)
    def __init__(self):
        self._dir=self.dir() 
        self._head=self._Node(None,None,None,self._dir)
        self._head._b=self._tail=self._Node(None,self._head,None,self._dir)
        self._valid=self.valid()
    def __len__(self):
        k=0
        pos = self.first()
        while pos:
            k+=1
            pos=self.after(pos)
        return k
    def is_empty(self):
        return len(self)==0
    def first(self):
        return self._make_position(self._head.next())
    def last(self):
        return self._make_position(self._tail.prev())
    def before(self,p):
        node=self._validate(p)
        return self._make_position(node.prev())
    def after(self,p):
        node=self._validate(p)
        return self._make_position(node.next())
    def __iter__(self):
        pos = self.first()
        while pos:
            yield pos.data()
            pos=self.after(pos)
    def _insert_after(self,data,node):
        newNode=self._Node(data,node,node.next(),self._dir)
        node.next().cprev(newNode)
        node.cnext(newNode)
        return self._make_position(newNode)
    def add_first(self,data):
        return self._insert_after(data,self._head)
    def add_last(self,data):
        return self._insert_after(data,self._tail.prev())
    def add_before(self,p,data):
        node=self._validate(p)
        return self._insert_after(data,node.prev())
    def add_after(self,p,data):
        node=self._validate(p)
        return self._insert_after(data,node)
    def delete(self,p):
        node=self._validate(p)
        data=node._data
        node.prev().cnext(node.next())
        node.next().cprev(node.prev())
        node.cprev(node.cnext(None))
        node._data=None
        return data
    def replace(self,p,data):
        node=self._valdiate(p)
        olddata=node._data
        node._data=data
        return olddata
    def rev_itr(self):
        pos = self.last()
        if len(self)==0:
            return self
        while pos:
            yield pos.data()
            pos=self.before(pos)
    def __iadd__(self,other): #[head,1,2,3,tail] [head a,b,c,tail]
        self.last()._node.cnext(other.first()._node)
        other.first()._node.cprev(self.last()._node)
        self._tail.cprev(other.last()._node)
        other.last()._node.cnext(self._tail)
        other._head.cnext(other._tail)
        other._tail.cprev(other._head)
        other._invalidate_positions()
        return self
        
    def split_after(self,p):     
        if (len(self)<=0):
            return self
        l=PList()
        l._head.cnext(self.after(p)._node)
        l._tail.cprev(self.last()._node)
        self.after(p)._node.cprev(l._head)

        p._node.cnext(self._tail)
        self.last()._node.cnext(l._tail)
        self._tail.cprev(p._node)

        self._invalidate_positions()

        print(l._dir._forward)
        print("head")
        print(l._head==l.first()._node.prev())
        print("tail")
        print(l._tail==l.last()._node.next())

        return l
        #L3=L2.split_before(L2.last())

    def split_before(self,p):
        return self.split_after(self.Position(self,p._node.prev()))

    def _invalidate_positions(self):
        self._valid.invalid()
        self._valid=self.valid()

    class dir:
        def __init__(self,forward=True):
            self._forward=forward

    def flip(self):
        h=self._head
        self._head=self._tail
        self._tail=h
        self._dir._forward=not self._dir._forward

#---------------CODE USED TO CHECK TESTS--------------------
def printList(L):
    print(" Forward:",list(L))
    print(" Backward:",list(L.rev_itr()))

def checkAnswer(taskno,testno,yours,correct):
    print("Task:",taskno," Test:",testno,end=" ")
    if yours==correct:
        print("Correct: ",yours)
    else:
        print("Wrong: ", yours," The correct answer is:")
        print(correct)

def checkList(taskno,testno,yours,correctforward):
    print("Task:",taskno," Test:",testno,end=" ")

    #print(yours._head.next())
    yoursforward=list(yours)
    yoursbackward=list(yours.rev_itr())
    correctbackward=correctforward.copy()
    correctbackward.reverse()
    if yoursforward==correctforward:
        if yoursbackward==correctbackward:
            print("Correct: ",yoursforward)
        else:
            print("Wrong! Your forward iterator is correct and gives ",
                  yoursforward,
                  " but your reverse iterator gives ",
                  yoursbackward)             
    else:
        print("Wrong. Your code gives ",yoursforward,
              " but the correct answer is:",correctforward)



#------------------------------------------------------
"""
To enable the test code for each task, change the booleans below. When you are
working on one task you may want to disable the others.
"""
testTask1=False
testTask2=False
testTask3=False
testTask4=False
testTask5=True


#------------------------TASK 1-----------------------
if (testTask1):
    print("\n------TASK 1------")
    L=PList()
    for i in range(5):
        L.add_first(i)
    printList(L) #Demo of the printList function, you may want to use to debug
    checkAnswer(1,1,len(L),5)
    checkAnswer(1,2,L.is_empty(),False)
    checkAnswer(1,3,len(PList()),0)
    checkAnswer(1,4,PList().is_empty(),True)

#------------------------TASK 2-----------------------
if (testTask2):
    print("\n------TASK 2------")
    L=PList()
    for i in range(5):
        L.add_first(i)
    L2=PList()
    for i in ("a","b","c","d","e"):
        L2.add_first(i)
    L+=L2
    checkList(2,1,L,[4, 3, 2, 1, 0, 'e', 'd', 'c', 'b', 'a'])
    checkList(2,2,L2,[])
#------------------------TASK 3-----------------------
if (testTask3):
    print("\n------TASK 3------")
    L=PList()
    for i in [1,2,"a","b"]:
        L.add_last(i)
    L2=L.split_after(L.after(L.first()))
    checkList(3,1,L,[1,2])
    checkList(3,2,L2,['a','b'])
    L3=L2.split_before(L2.last())
    checkList(3,3,L2,['a'])
    checkList(3,4,L3,['b'])
    L4=L3.split_before(L3.first())
    checkList(3,5,L3,[])
    checkList(3,6,L4,['b'])
    

#------------------------TASK 4-----------------------
if (testTask4):
    print("\n------TASK 4------")
    L=PList()
    for i in range(5):
        L.add_first(i)
    p=L.last()
    L2=L.split_before(L.before(p))
    try:
        q=L.before(p)
    except ValueError:
        print("Task: 4 Test:1 Correctly has an exception")
    else:
        print("Task: 4 Test:1 Wrong! No exception")
    try:
        q=L2.before(p)
    except ValueError:
        print("Task: 4 Test:2 Correctly has an exception")
    else:
        print("Task: 4 Test:2 Wrong! No exception")
    p=L.first()
    p2=L2.first()
    try:
        p=L.after(p)
        p2=L2.after(p2)
        L+=L2
        p=L.before(p)
    except ValueError:
        print("Task: 4 Test:3 Wrong! There should be no exception")
    else:
        print("Task: 4 Test:3 Correct, no exception")
    try:
        p2=L2.before(p2)
    except ValueError:
        print("Task: 4 Test:4 Correctly has an exception")
    else:
        print("Task: 4 Test:4 Wrong! No exception")
    

#------------------------TASK 5-----------------------
if (testTask5):
    print("\n------TASK 5------")
    L=PList()
    for i in range(5):
        L.add_first(i)

#checking the basic flip operation
    L.flip()
    checkList(5,1,L, [0, 1, 2, 3, 4])
    L2=PList()
    for i in ("a","b","c","d","e"):
        L2.add_first(i)
#checking the += works with flip
    L+=L2
    checkList(5,2,L,[0, 1, 2, 3, 4, 'e', 'd', 'c', 'b', 'a'])
    checkList(5,3,L2,[])

#checking that split works with flip
    L=PList()
    for i in [1,2,"a","b"]:
        L.add_last(i)
    L.flip()

    L2=L.split_after(L.after(L.first()))
    checkList(5,4,L2,[2,1])
    checkList(5,5,L,['b','a'])

    print('L3')
    L3=L2.split_before(L2.last())
    print("head")
    print(L3._head==L3.first()._node.prev())
    print("tail")
    print(L3._tail==L3.last()._node.next())

    L.flip()
    
    checkList(5,6,L2,[2])
    checkList(5,7,L3,[1])

    print(L3._dir._forward)
    print("head")
    print(L3._head==L3.first()._node.prev())
    print("tail")
    print(L3._tail==L3.last()._node.next())

    ###
    L4=L3.split_before(L3.first())
    checkList(5,8,L3,[])
    checkList(5,9,L4,[1])

#checking the positions move in the right direction always
    L=PList()
    for i in range(5):
        L.add_last(i)
    p=L.after(L.first())
    checkAnswer(5,10,(L.before(p).data(),L.after(p).data()),(0,2))
    L.flip()
    checkAnswer(5,11,(L.before(p).data(),L.after(p).data()),(2,0))
 
       
    
    
