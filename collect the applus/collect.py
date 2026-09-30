import pgzrun
import random

WIDTH=600
HEIGHT=500

score=0

apple=Actor("appkle")

bob=Actor("bakket")

bob.y=400
bob.x=250

apple.x=random.randint(50,WIDTH-50)

def draw():
    screen.blit("garden",(0,0))
    apple.draw()
    bob.draw()
    screen.draw.text(str(score),(0,0))

def update():
    global score
    apple.y+=5
    if apple.y>HEIGHT:
        apple.y=0
        apple.x=random.randint(50,450)

    if keyboard.left:
            bob.x-=10
    if keyboard.right:
            bob.x+=10        

    if bob.colliderect(apple):
        score+=1
        apple.y=0
        apple.x=random.randint(50,450)
          



pgzrun.go()