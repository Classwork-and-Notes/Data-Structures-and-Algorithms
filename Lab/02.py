import turtle
import math
import random

def randomColor():
    """Code is not used here but you may find it usefull"""
    return [random.random() for i in range(3)]

def draw():
	"""This draw function will be repeatedly called"""
	turtle.clear()
	turtle.penup()
	turtle.goto(0,0)
	ss.draw()
	global angle #Python requires this to change a global variable
	angle+=0.01 
	screen.ontimer(draw,0) #This tells the system to call this function again as soon as possible

class Sun:
	def __init__(self,center,size,color):
		self._center=center
		self._size=size
		self._color=color
	def draw(self):
		turtle.dot(self._size*2,self._color)
	def getCenter(self):
		return self._center
	def getSize(self):
		return self._size
	def setColor(self,color):
		self._color=color
	def setSize(self,size):
		self._size=size
	def inside(self,location):
		a=[math.pow(x-y,2) for x,y in zip(self._center, location)] #a^2 an b^2
		if self._size >= math.sqrt(a[0]+a[1]):
			return True
		else:
			return False
	def onClick(self,location):
		if self.inside(location):
			print(self)
			global last
			last=self
			self.setColor(randomColor())


class Planet(Sun):
	def __init__(self,orbitAround,orbitRadius,size,color,speed):
		self._size=size
		self._color=color
		self._orbitAround=orbitAround
		self._orbitRadius=orbitRadius#rand(self._size//2+orbitAround.getSize()) #based on planet size and orbiting body size
		self._speed=speed
	def getRadius(self):
		return self._orbitRadius
	def setRadius(self,orbitRadius):
		self._orbitRadius=orbitRadius
	def move(self):
		self._center=[x+self._orbitRadius*f(angle*self._speed)
              for x,f in zip(self._orbitAround.getCenter(), (math.sin,math.cos))]
		self.draw(self._center,self._size,self._color)
	def draw(self,location,size,color):
		turtle.penup()
		turtle.goto(*location)
		turtle.dot(size*2,color)

def randInt():
	return random.randrange(5)+1 #1-4

def randSpeed():
	return random.random()

def rand(x,y=0):
	return random.randrange(y,x)+1 

class SolarSystem:
	def __init__(self):
		self._sun=Sun( (0,0), 30, "yellow")
		sSize=self._sun.getSize()
		self._planets=[]
		self._moons=[]
		for i in range(randInt()):
			#orbitAround, orbitRadius, size,color,speed
			self._planets.append(Planet(self._sun, rand(300, sSize),rand(sSize*3//4, 10), "red", randSpeed()))
		for p in self._planets:
			for i in range(randInt()):
				self._moons.append(Planet(p, rand(100, p.getSize()), rand(p.getSize()*3//4, 3), "blue", randSpeed()))
		self._planets=self._planets+self._moons

	def draw(self):
		self._sun.draw()
		for planet in self._planets:
			planet.move()
	#		planet.draw()
	def onClick(self,location):
		self._sun.onClick(location)
		for planet in self._planets:
			planet.onClick(location)
	def add(self, p):
		self._planets.append(p)

def onClick(x,y):
	ss.onClick((x,y))

def keyRight():
	last.setRadius(last.getRadius()+1)

def keyLeft():
	last.setRadius(last.getRadius()-1)

def keyUp():
	last.setSize(last.getSize()+1)

def keyDown():
	last.setSize(last.getSize()-1)

def space():
	last.setColor(randomColor())

def add():
	ss.add(Planet(last, rand(100, last.getSize()*2), rand(last.getSize()*3//4, 3), "blue", randSpeed()))

ss=SolarSystem()

last=0
angle=0 
turtle.tracer(0,0)
turtle.ht() 
screen=turtle.Screen() #Needed for the following
screen.onkey(turtle.bye,"q") #quits if you press q
screen.ontimer(draw,0) #Tells the system to call draw. Don't call it directly
screen.onclick(onClick)
screen.onkey(keyRight, "Right")
screen.onkey(keyLeft, "Left")
screen.onkey(keyUp, "Up")
screen.onkey(keyDown, "Down")
screen.onkey(space, "space")
screen.onkey(add, "n")
screen.listen() 
turtle.mainloop()