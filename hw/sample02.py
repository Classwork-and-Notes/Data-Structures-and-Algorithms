  #1
def odd_iter(self):
	p=self.first()
	while p:
		yield p.data()
		if self.after(p):
			p=self.after(self.after(p))
		else:
			p=None

#2
def swap_forward(self,p):
	here=p._node
	before=p._node._prev
	next=p._node._next
	nnext=p._node._next._next

	#here._next, here._prev, next._next next._prev = next._next next._prev, here._next, here._prev
	#before._next, nnext._prev = nnext._prev, before._next
	before._next=next
	next._prev=before
	here._next=nnext
	nnext._prev=here
	here._prev=next
	next._after=here

#3
def _add_left(self,p,e):
	node = self._validate(p)
	if node._left is not None:
		raise ValueError('Left child exists')
	self._size += 1

	node._left = self._Node(e, node, node._prev, node)
	node._prev._next = self._node._left
	node._prev = self._node._left
	return self._make_position(node._left)

#4
def stringTree(s)
	t = Tree()
	t.add_root(None)

	stringNode(t._root)

	def stringNode(s,node):
		if len(s) == 0:
			return

		node._data = s
		mid = len(s)/2

		node._left = stringTree(s[:mid], t._Node(None,node))
		node._right = stringTree(s[mid:], t._Node(None,node))

	return t

#5
def kthMin(self, k):
	a=[]
	for i in range(k):
		A.append(self._remove_min())
	r=A[-1]
	for i in range(k):
		self.add(*i)
	return r
# * expands tuple 

#6
def sim:
	def __init__(self, days):
		self._days=days
		self._bulbs=[randint(100,110) for i in range (100)]
	def run(self):
		most=0
		for x in range(self._days):
			today=0
			for i in range(100):
				self._bulbs[i]-=1
				if self._bulbs[i]==0:
					print("Day " + str(s) +": Light bulb " + str(i))
					self._bulbs[i] = randint(100,110)
					today+=1
			if today>most:
				most=today
		print(most)

"""
c={}
H=heap()
for i in range(100):
	H.add(randint(100,110),1)
while :
	(t,id)=H.extract-min()
	print whatever
	H.add(t+randint(100,110),id)
if t in c:
	c[t]+=1
else:
	c[t]=0

?????return max(c.values())
"""

def diffstr(l):
	d={}
	for i in l:
		if d[i]:
			d[i]+=1
		else:
			d[i]=0
	str=""
	for key in d:
		if d[key]>d[str]
		str=key
	return str
#O(2n)=O(n) efficiency

#7
4,2,6,1,3,5,7 
#8
#do i have to write somethign for this????