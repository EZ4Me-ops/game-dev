import pgzrun
import random
import time
WIDTH=400
HEIGHT=400
satalite_data=[]
lines_data=[]
current_satalite=0
total_satalite=6
start_time=0
total_time=0

for i in range(total_satalite):

    statilite=Actor("satalite.png")
    statilite.x=random.randint(10,WIDTH-10)
    statilite.y=random.randint(10,HEIGHT-10)
    satalite_data.append(statilite)

start_time=time.time()
def draw ():
    screen.blit("stars.png",(0,0))
    sat_number=1
    for sat in satalite_data:
        sat.draw()
        screen.draw.text(str(sat_number),(sat.x,sat.y+20)) 
        sat_number+=1
    for lines in lines_data:
        screen.draw.line(lines[0],lines[1],"blue")    
    screen.draw.text(str(total_time),(20,20 ))    


def on_mouse_down(pos):
    global current_satalite,lines_data
    if current_satalite<total_satalite:
        if satalite_data[current_satalite].collidepoint(pos):# the current satalite positon
            if current_satalite!=0:
                current_satalite_pos=satalite_data[current_satalite].pos
                previous_satalite_pos=satalite_data[current_satalite-1].pos
            
                lines_data.append([current_satalite_pos,previous_satalite_pos])
            current_satalite+=1
            print(lines_data)
        else:
            lines_data=[]
            current_satalite=0

def update():
    global total_time
    if current_satalite<total_satalite:
        total_time=time.time()-start_time
pgzrun.go()
    