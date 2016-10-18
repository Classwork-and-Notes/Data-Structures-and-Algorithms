
def rev(l):
	if len(l):
		return rev(l[1:])+[(l[0])]
	else:
		return l

A=[1,2,3,4]
B=rev(A)
print(B)

def s(l):
		if isinstance(l, list):
				return s(l[0])+s(l[1:])
		else:
			return [l]

A=[1,[2,5],2,3,4]
B=s(A)
print(B)

def tr(A,x,y):
	#return A[x][y]+ max(tr(A[x-1][y]) if x > 0 else 0,tr(A,[x][y-1]) if y > 0 else 0) 
	if x and y:
		return A[x][y]+max(tr(A[x-1][y]),tr(A,[x][y-1]))
	else:
		return 0