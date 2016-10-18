def setup():
    size(60, 60)
    background(255)
    pixelDensity(displayDensity())
    global pause
    pause=False
    global cells
    cells=[[0]*(height//20) for i in range(width//20)]
    for y in range (0,height,20):
        for x in range (0,width,20):
            #print(x//20,y//20)
            cells[x//20][y//20]=cell((x,y),(x//20,y//20))
    randLive()
    frameRate(1)
    print("start")

def randLive():
    for i in cells:
        for j in i:        
            if int(random(2)):    
                j.live()

def draw():
    if not pause:
        print("go")
        clear()
        for i in cells:
            for j in i:
                #print(j.getPos[0])
                #print(j.isAlive())
                if j.isAlive():
                    fill(255)
                    stroke(0)
                else:
                    stroke(255)
                    fill(0)
                rect(j.getPos()[0],j.getPos()[1], 40, 40)
                dex=j.getIndex()
                neigh=0
                print(dex,"check")
                for x in range(-1,2):
                    if 0<=dex[0]+x<len(cells):
                        for y in range(-1,2):
                            if 0<=dex[1]+y<len(cells[x]):
                                print(dex[0]+x,dex[1]+y)
                            
                                if cells[dex[0]+x][dex[1]+y].isAlive():
                                    print("alive")
                                    neigh+=1
                                    #print(neigh)
                #print(j.isAlive())
                if j.isAlive():
                    neigh-=1
                    #print(neigh)
                if j.isAlive():
                    if neigh<2:
                        j.live()
                    elif neigh>3:
                        j.live()
                else:
                    if neigh==3:
                        j.live()                                   
                
            
def keyPressed():
    if key==" ":
        global pause
        pause = not pause
    if key=="r":
        randLive()
    if key=="n":
        for i in cells:
            for j in i: 
                if j.isAlive():
                    j.live()
    

def mousePressed():
    cells[mouseX//20][mouseY//20].live()

    
class cell:
    def __init__(self,pos,index):
        self._alive=False
        self._pos=pos
        self._index=index
    def live(self):
        self._alive=not self._alive
    def getPos(self):
        return self._pos
    def isAlive(self):
        return self._alive
    def getIndex(self):
        return self._index
    
    
        