Binary Search Tree

#position if found
#closest position if not exist
def _subtree_search(self,p,k):
	if k==p.key():
		return p
	if k>p.key():
		if self.right(p):
			return self._subtree_search(self.right(p),k)
		else:
			return p
	if k<p.key():
		if self.left(p):
			return self._subtree_search(self.left(p),k)
		else:
			return p

def find_position(self,k):
	return self._subtree_search(self.root(),k)

def __contains__(self,k):
	return self.find_position(k).key()==k

#leftmost position
def _subtree_first_position(self,p):
		if self.left(p):
			return self._subtree_search(self.left(p))
		else:
			return p

def find_min(self):
	return self._subtree_first_position(self.root())

def after(self,p):
	if self.right(p):
		return self._subtree_first_position(self.right(p))
	else:
		r=self.parent(p)
		while r and r.key()<p.key():
			r=self.parent(r)
		return r

def __iter__(self):
	p=self._subtree_first_position(self.root())
	while p:
		yield p.key()
		p=self.after(p)

def __setitem__(self,k,v):
	p=self.find_position(k)
	if p.key()==k:
		p.data()._value=v
	else:
		if k>p.key():
			self._insert_right(p,k,v)
		if k<p.key():
			self._insert_left(p,k,v)

def __getitem__(self,k):
	p=self.find_position(k)
	if p.key()==k:
		return (p.key(),p.value())
	else:
		raise ValueError("errrrr")

def delete(self,p):
	if self.num_children<2:
		super().delete()
	else:
		r=self.before(p)
		p.data()._value=r.data._value
		p.data()._key=r.data._key
		self.delete(r)

