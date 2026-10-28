import os 
os.environ["SDL_VIDEO_WINDOW_POS"] ="50,50"

import pgzrun
WIDTH=800
HEIGHT=900

drawing=False

points=[]

button1=Rect(150,25,50,50)

button2=Rect(250,25,50,50)

button3=Rect(350,25,50,50)

button4=Rect(450,25,50,50)


color="black"

def draw():
    screen.fill("white")
    for point,c in points:
        screen.draw.filled_circle(point,3,c)
    screen.draw.text("choose a color from below!!!!!!!!",(0,0),color="black")
    screen.draw.filled_rect(button1,"red")
    screen.draw.filled_rect(button2,"black")
    screen.draw.filled_rect(button3,"sky blue")
    screen.draw.filled_rect(button4,"white")
    screen.draw.textbox("erasor",button4,color="black")
    

def on_mouse_down(pos):
    global drawing,color
    drawing=True
    if button1.collidepoint(pos):
        color="red"
    if button2.collidepoint(pos):
            color="black"
    if button3.collidepoint(pos):
            color="sky blue"
    if button4.collidepoint(pos):
                color="white"
        

def on_mouse_up(pos):
    global drawing
    drawing=False


def on_mouse_move(pos):
    if drawing:
        points.append([pos,color])
        print(points)


pgzrun.go()