import pgzrun 
import random
import time
WIDTH=1000
HEIGHT=800
satellites=[]
lines=[]
next=0
starttime=0
totaltime=0
endtime=0
numberofsatellite=8
def createsatellite():
    global starttime
    for i in range (0,numberofsatellite):
        satellite=Actor('satelliet')
        satellite.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
        satellites.append(satellite)
    starttime=time.time()
def draw():
    global totaltime
    screen.blit('sky',(0,0))
    number=1
    for i in satellites:
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        i.draw()
        number=number+1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))
    if next<numberofsatellite:
        totaltime=time.time()-starttime
        screen.draw.text(str(round(totaltime,1)), (10,10), fontsize=30)
    else:
        screen.draw.text(str(round(totaltime,1)), (10,10), fontsize=30)
    
def update():
    pass

def on_mouse_down(pos):
    global next, lines

    if next < numberofsatellite:
        if satellites[next].collidepoint(pos):
            if next:
                lines.append((satellites[next-1].pos, satellites[next].pos))
            next=next + 1
        else:
            lines=[]
            next=0
createsatellite()

pgzrun.go()
            
    






