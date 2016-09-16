'''
runtimes - big O aka asymptotic notation
little omega ">" write biggest
big omega ">=" can it be trapped above
big thetha keep biggest term of n "=" write smallest
big o "<="
little o "<"


---slow
x^N
N^x
Nlog2(N)
N
root(N)
log2(N)
1
fast---

def inAllThree(A,B,C):
	for a in A:
		for b in B:
			if a==b: 
				for c in C:  --->runs n times 
					if a==c:
						return True
					else 
						return False

this is a n^2 operation
'''