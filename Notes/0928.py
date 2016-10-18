A=[1,2,3] #list
B=(1,2,3) #tuple, immutable
print(A[1],B[1])

A[1]=5
B[1]=5 #xx does not work

#strings are immutable

#inefficient
s="some string"
T=""
for c in s:
	if c.isaplha():
		T+=c
#better
T=[]
for c in s:
	if c.isaplha():
		T.append(c)
A="".join(T) #something like this

#even better
A="".([c for c in s if c.isalpha()])

#best
A="".(c for c in s if c.isalpha()) #join takes iterable, list comprehension is a iterator

def s(A):
	r=0
	for i in A:
		r+=i
	return r

def f():
	for i in range(5):
		yeild i

s(f()) #constant memory
s([i for i in f()]) #intermediary result

#big o of common functions
A[5] #O(1)
A[i:j] #O(j-1)
A.append(5) #O(1)
A.pop() #O(1)
A+B # both A and B are lists O(len(A)+len(B)
5 in A #O(n)
A.index(5) #O(n)
A==B #O(n)
c*A #c is a number, O(cn)
del A[2] #O(n-i) aka O(n)
A.count(5) #O(n)
del A #undeclars A as a variable, A doesn't exist
A.sort() #O(nlogn)


A=[0,1,5,7,2]
B=[0,1,4,8,9]
#is A<B?
#looks through corresponding elements

#stacks
#push add to top
#pop removes from top
#top returns top object

class stack:
	def __init__(self):
		self._A=[]
	def push(self,x):
		self._A.append(x)
	def pop(self):
		self._A.pop()
	def top(self):
		return self.A[-1]
	def __len__(self):
		return len(self._A)

def pmatch(str):
	open="({["
	close=")}]"
	s=stack()

	for c in str:
		if c in open:
			s.push(c)
		else:
			if c=close[open.index(s.top)]:
				s.pop()
			else:
				return false
	return s.isEmpty()

	#queues
	#enqueue adds to back
	#dequeue removes from front
	#front returns front duh
	#back returns back

class queue:
	def __init__(self):
		self._A=[None]
		self._back=0
		self._front=0
	def enqueue(self,x):
		if front=(back+1)%len(A) #this shit can also be done with list concatnation
			B=[None]*len(A)*2
			i=front
			while i != back:
				B[j]=A[i]
				i=(i+1)%len(A)
				j=j+1
			B[j]=A[i]
			A=B
		else:
			back=(back+1)%len(A)
			A[back]=x
			
	def dequeue(self):
		self._front=(self.front+1)%len(A)
	def front(self):
		return self._A[self._front]
	def back(self):
		return self._A[self._back]
	def __len__(self):
		return len(self._A)

# collections.deque
# append()
# pop()
# appendleft()
# popleft() something like this

