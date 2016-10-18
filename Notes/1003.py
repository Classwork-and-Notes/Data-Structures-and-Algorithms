class C:
	__slots__==("x","y") #declares variables, no other variables can be declared, c.__dict__ will fail 
	__init__(self,x,y):
		self._x,self._y=x,y

c=C(5,7)
c.__dict__ #returns a dictionary of all variable names and their variables, all variable names are strings