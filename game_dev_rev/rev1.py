import pgzrun
import random  

WIDTH=500
HEIGHT=500

person=Actor("appkle")
person.x=random.randint(0,WIDTH)
person.y=random.randint(0,HEIGHT)

message=""

def draw():
    # screen.fill("maroon")
    screen.blit("miles",(0,0))
    person.draw()
    screen.draw.text(message,(0,0))

def on_mouse_down(pos):
    global message
    print(pos)
    if person.collidepoint(pos):
        message="good person"
        person.x=random.randint(0,WIDTH)
        person.y=random.randint(0,HEIGHT)
pgzrun.go()
