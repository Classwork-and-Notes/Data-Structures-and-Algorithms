#Just Call draw_tree on the root node and it will draw the tree
#Your node class must use ._l ._r and ._data
import random

def subtree_size(node):
    if node is None:
        return 0
    else:
        return 1+subtree_size(node._l)+subtree_size(node._r)
def draw_tree(node,level=1,x=20,parx=None,pary=None):
    XSEP=15
    YSEP=30
    fill(0)
    textAlign(CENTER,CENTER)
    textSize(15)
    #print(node._data)
    lsize=subtree_size(node._l)
    myx,myy=x+lsize*XSEP,YSEP*level
    text(str(node._data),myx,myy)
    if node._l is not None:
        draw_tree(node._l,level+1,x,myx,myy)
    if node._r is not None:
        draw_tree(node._r,level+1,x+(lsize+1)*XSEP,myx,myy)
    if parx is not None:
        strokeWeight(10)
        stroke(0,255,0,30)
        line(parx,pary,myx,myy)

class PQ:
    class _Node:
        def __init__(self,data,l=None,r=None):
            self._l=l
            self._r=r
            self._data=data
    def __init__(self):
        self._root = None #self._Node(None)
        self._size = 0
    def add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)
        
    def merge(self,node,other):             
        if node==None:
            return other
        elif other==None:
            return node    
        # print(list(self))
        
        if node._data<other._data:
            #print("node")
            node._l=self.merge(node._l,other)
            return node
        else:
            #print("other")
            other._l=self.merge(other._l, node)
            return other
        
        
    def flip(self):
        print("flip")
        left=self._root._l
        self._root._l=self._root._r
        self._root._r=left
        while left:
            #print(left._data)
            next=left._l
            left._l=left._r
            left._r=next
            left=next
            
    def insert(self,k):
        #print("insert")
        node=self._Node(k)
        self._root=self.merge(self._root,node)
        #print(self._root)
        self.flip()
        
    def extractMin(self): 
        root=self._root
        self.merge(root._l,root._r)
        return root._data

# pq=PQ()
# pq._root=root=pq._Node(0)
# root._l=pq._Node(2)
# root._r=pq._Node("a")
# o=PQ()  
# o._root=oroot=o._Node(1)
# oroot._l=o._Node(3)
# oroot._r=o._Node("b")   
# print(list(pq))
# print(list(o))
# pq.merge(o)
# print(list(pq))

# A=list(range(20))
# #random.shuffle(A)
# pq=PQ()
# for i in A:
#     print(i)
#     pq.insert(i)
# print([pq.extractMin() for i in range(20)])

def setup():
    size(1200, 1000)
    background(255)
    
    #pixelDensity(displayDensity())
    #frameRate(1)
def draw():
    #clear()
    A=list(range(20))
    #random.shuffle(A)
    pq=PQ()
    for i in A:
        pq.insert(i)
    draw_tree(pq._root)
    #print([pq.extractMin() for i in range(20)])
    noLoop()