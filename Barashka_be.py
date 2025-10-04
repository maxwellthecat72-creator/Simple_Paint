from turtle import *

t = Turtle()

t.shape('circle')
t.color('blue')
t.pensize(5)
t.speed(0)
def draw(x,y):
    t.goto(x,y)
t.ondrag(draw)
def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
scr = t.getscreen()
scr.listen()
scr.onscreenclick(move)

def tcolor_green():
    t.color('green')
    t.pensize(5)
def tcolor_purple():
    t.color('purple')
    t.pensize(5)
def tcolor_red():
    t.color('red')
    t.pensize(5)
def tcolor_yellow():
    t.color('yellow')
    t.pensize(5)
def tcolor_black():
    t.color('black')
    t.pensize(5)
def tcolor_cyan():
    t.color('cyan')
    t.pensize(5)
def tcolor_white():
    t.color('white')
    t.pensize(20)

def eraser():
    t.clear()

scr.onkey(tcolor_green, 'g')
scr.onkey(tcolor_purple, 'p')
scr.onkey(tcolor_red, 'r')
scr.onkey(tcolor_yellow, 'y')
scr.onkey(tcolor_black, 'b')
scr.onkey(tcolor_cyan, 'c')
scr.onkey(tcolor_white, 'w')
scr.onkey(eraser, 'Backspace')



def move_up():
    t.goto(t.xcor(), t.ycor() + 5)
def move_down():
    t.goto(t.xcor(), t.ycor() - 5)
def move_left():
    t.goto(t.xcor() - 5, t.ycor() )
def move_right():
    t.goto(t.xcor() + 5, t.ycor())

scr.onkey(move_up, 'Up')
scr.onkey(move_down, 'Down')
scr.onkey(move_left, 'Left')
scr.onkey(move_right, 'Right')

def bebegin_fill():
    t.begin_fill()

def enend_fill():
    t.end_fill()

scr.onkey(bebegin_fill, 'z')
scr.onkey(enend_fill, 'x')












