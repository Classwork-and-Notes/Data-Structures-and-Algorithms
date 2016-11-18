l=["hello","you","abd","i"]

def mostFrequent(A):
	m={}
	for w in A:
		m[w]=m.get(w,0)+1
	return max(m.items(),key=lambda x:x[1])[0]
	#single in-line functions lambda

def hash(t):
	value=345678
	for item in t:
		value=10000003*value^item#^ is XOR, represent in bits, 0 if same, 1 if different

class htable:
	def __init__(self):
		self._A=[[] for i in range(10)]
		self._size=0
		self._deleted=Object()
	def __getitem__(self,k):
		for (key,val) in self._bucket(k):
			if key==k:
				return val
		raise KeyError("not found")
	def _bucket(self,k):
		return self._A[hash(k)%len(self._A)]
	def __setitem__(self,k,v):
		b=self._bucket(k)
		for i in range(len(bucket)):
			if b[i][0]==k:
				b[i]=(b[i][0],v)
				return
		b.append((k,v))
		self._size+=1
		if self._size>2*len(self._A):
			self._resize(2*len(self._A))

	def __del__(self,k,v):
		b=self._bucket(k)
		for i in range(len(bucket)):
			if b[i][0]==k:
				b.pop(i)
				return
				self._size-=1

	def _resize(self,ns):
		D=self.items()
		self._A=[[]for i in ns]
		self._size=0
		for k,v in D:
			self[k]=v