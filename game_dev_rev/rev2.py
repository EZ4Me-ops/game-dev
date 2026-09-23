import pgzrun

WIDTH=500
HEIGHT=500

person=Actor("appkle")

def draw():
    screen.blit("miles",(0,0))
    person.draw()


def update():
    if keyboard.D:
        person.x+=10
    if keyboard.S:
        person.y+=10
    if keyboard.W:
        person.y-=10
    if keyboard.A:
        person.x-=10
    

#only works once per press
def on_key_down(key):
    if key==keys.S:
        person.y+=10
    



pgzrun.go()