#w and s key controls length of branch
#a and d key controls how many layers there are/how many times it branches
#to test hold w,a,s,d keys
import sys
import random
import math
from itertools import cycle
def setup():
    global leaf
    global txt
    global len
    global lay
    global ran
    li = range(-45, 46) + range(45, -46, -1)
    ran=cycle(li)
    sway=0
    leaf=True
    txt=True
    lay=3
    len = 100
    size(1100, 800)
    background(255)
    pixelDensity(displayDensity())
    frameRate(30)
    
def drawLineAngle(color, start, angle, length, width=1):
    angle += 180 # make up zero degrees
    end = (start[0] + math.sin(math.radians(angle)) * length,
    start[1] + math.cos(math.radians(angle)) * length)
    stroke(*color)
    if width:
        strokeWeight(width)
    else:
        noStroke()
    line(*(start + end))
    return end

def num(pos):
    global leaf
    strokeWeight(1)
    global branch
    fill(0,255,0)
    ellipse(pos[0],pos[1],15,15)
    fill(0)
    textSize(16)
    text(branch,pos[0],pos[1],100)

def drawLeaf(location,width):
    stroke(0, 50, 0)
    fill(100, 255, 100)
    strokeWeight(0.5)
    ellipse(location[0],location[1],width,width)
    
def drawTree(layer,start,angle,length, width):
    if layer:
        end = drawLineAngle((255,0,0),start,angle,length,width)
        global txt
        if txt:
            num(end)
        global sway
        global branch
        branch +=1
        drawTree(layer-1,end,angle+30+sway*1.3,length*.75,width*.7)
        drawTree(layer-1,end,angle-30+sway*1.3,length*.75,width*.7)
    global leaf
    if leaf and layer==1:
        drawLeaf(end,width*7)
        global txt
    
def keyPressed():
    global leaf
    global txt
    if key=="l":
        leaf = not leaf
    if key=="n":
        txt = not txt
    global len
    if key=="w":
        len+=1
    if key=="s":
        len-=1
    global lay
    if key=="d":
        lay+=1
    if key=="a":
        lay-=1

    
def draw():
    clear()
    global branch
    branch=0
    global len
    global lay
    global sway
    li = range(-60, 61) + range(60, -61, -1)
    # sway+=1
    # if sway==60:
    #     sway=-1*sway
    global ran
    sway=next(ran)*.3
    background(255)
    drawTree(lay,(550,400),sway,len,5)