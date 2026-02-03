import pgzrun
import random
WIDTH=400
HEIGHT=400
satalite_data=[]
lines_data=[]

for i in range(5):

    statilite=Actor("satalite.png")
    statilite.x=random.randint(10,WIDTH-10)
    statilite.y=random.randint(10,HEIGHT-10)
    satalite_data.append(statilite)


def draw ():
    screen.blit("stars.png",(0,0))
    sat_number=1
    for sat in satalite_data:
        sat.draw()
        screen.draw.text(str(sat_number),(sat.x,sat.y+20)) 
        sat_number+=1


pgzrun.go()
    