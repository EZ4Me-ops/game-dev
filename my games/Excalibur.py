import os 
os.environ["SDL_VIDEO_WINDOW_POS"] ="50,50"

import pgzrun
WIDTH=800
HEIGHT=900

drawing=False

points=[]

color="black"

def draw():
    screen.fill("white")
    for point in points:
        screen.draw.filled_circle(point,3,color)

def on_mouse_down(pos):
    global drawing
    drawing=True

def on_mouse_up(pos):
    global drawing
    drawing=False

def on_mouse_move(pos):
    if drawing:
        points.append(pos)
        print(points)

pgzrun.go()