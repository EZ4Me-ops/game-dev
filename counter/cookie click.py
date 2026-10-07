
import pgzrun

WIDTH = 600
HEIGHT = 500

score = 0

cookie = Actor("choclat")
cookie.x = 300
cookie.y = 250

def draw():
    screen.fill((255,255,255))
    cookie.draw()
    screen.draw.text(str(score),(550,10),color="blue")

def on_mouse_down(pos):
    global score
    if cookie.collidepoint(pos):
        score += 1
        cookie.x = pos[0]
        cookie.y = pos[1]

pgzrun.go()