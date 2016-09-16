#class creation python
class Counter:
	def __init__(self):
		self._c #underscore denotes private variable
	def inc(self):
		self._c+=1
	def __str__(self):
		return str(self._c)

c=Counter()
print(c) #0
c.inc()
print(c) #1
d=c
d.inc()
print(c,d) #2,2 because d and c points to same objects

#Copying
class Counter:
	def __init__(self,c=None):
		if (c==None):
			self._c=0
		else:
			self.c=c._c
	def inc(self):
		self._c+=1
	def __str__(self):
		return str(self._c)

c=Counter()
for i in range(1000):
	c.inc
d=Counter(c)
import copy
e= copy.copy(c)

A=[]
A.append(Counter())
for i in range(4):
	A.append(copy.copy(A[0])) #new objects
A+=copy.copy(A) #new arrary but referrs to same objects
A[1].inc() 
print(A) #0100001000
#use copy.deepcoy to copy everything

#static variables
class Counter:
	numcounters= n
	def __radd__(self,x):
		self._c+=x

c=Counter()
c=c+15
c=15+c

class Counter:
	numcounters=n #static variable, shared by all counters
	def __init__(self):
		self._c=0
		Counter.numcounters+=1
	def getnc():
		return Counter.numcounters

A[Counter() for i in range(10)]
print(Counter.getnc())

#Inheritance
class FancyCounter(Counter):
	def __init__(self, step):
		super().__init__() #do init of Counter class
		self._step = 
	def inc(self):
		self._c+=self._step
	class _huh(object): #not inheritance, class inside of a class

#throwing exceptions
throw StopIteration
try:
	#code goes here
except StopIteration:

#iterations
for i in range(10):
	B=[1,2,3,4]
	A=[i+1 for i in B] #[2,3,4,5]	

I=iter([1,2]) #iterator class, supports __next__ and __iter__, which returns itself
print(next(I)) #1
print(next(I)) #2 etc
print(next(I)) #crash!! StopIteration

class CountIter:
	def __iter__():
		return self
	def __init__(self,c,l): #c is the counter and l is the limit
		self._c=c
		self._l=l
	def __next__():
		self._c.inc()
		if (self._c.value() <= self._l):
			return self._c.value()
		else:
			throw StopIteration

for i in CountIter(FancyCounter(4),20):
	print i #0,4,8,14,16

'''
for i in x means:
I=iter(x)
while True:
	try:
		I.next()
	except StopIteration:
		break
'''

def CoIgen(c,l):
	while c.value < l:
		yield c.value
		c.inc()