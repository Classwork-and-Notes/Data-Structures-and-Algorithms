import turtle
import timeit

def fib1(n):
	if n == 0:
		return 0
	elif n <= 2:
		return 1
	else:
		return fib1(n-1) + fib1(n-2)

print([fib1(i) for i in range(10)])

def fib2(n):
	a = []
	a.append(0)
	if n > 0:
		a.append(1)
	for x in range(n-1):
		a.append(a[-1] + a[-2])
	return a[-1]

print([fib2(i) for i in range(10)])

def fib3(n):
	if n == 0:
		return 0
	a = 0
	b = 1
	for x in range(n-1):
		a, b = b, a + b
	return b

print([fib3(i) for i in range(10)])

def timeFunction(f,n,repeat=1):
	return timeit.timeit(f.__name__+'('+str(n)+')',
		setup = "from __main__ import " + f.__name__, number = repeat)/repeat

def printFunctionTimes(list, range):
	s = ""
	for i in range:
		s += "n=" + str(i) + ":" 
		for k in list:
			s += " " + str(timeFunction(k, i))
		s += "\n"
	print(s)

#printFunctionTimes((fib1,fib2,fib3), range(5,40,5))
def plotFunctionTimes(functions, colors, xrange, maxy, repeat = 1):
	turtle.setworldcoordinates(0,0,xrange[-1],maxy)
	turtles = []
	for c in colors:
		turtles.append(turtle.Turtle())
		turtles[-1].pencolor(c)

	for i in xrange:
		for t,f in zip(turtles,functions):
			t.goto(i,timeFunction(f,i,repeat))	

	#for f,c in zip(functions, colors):
	#	t = turtle.Turtle()
	#	t.pencolor(c)
	#	for i in xrange:
	#		t.goto(i,timeFunction(f,i,repeat))

plotFunctionTimes((fib2,fib3),("black","red"),range(1,100,2),0.0002,repeat = 10)