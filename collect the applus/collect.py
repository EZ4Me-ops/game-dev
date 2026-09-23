import pgzrun
import random

WIDTH=500
HEIGHT=500

apple=Actor("appkle")

apple.x=random.randint(50,WIDTH-50)

def draw():
    screen.blit("miles",(0,0))
    apple.draw()


def update():
    apple.y+=5


pgzrun.go()