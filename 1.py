import turtle
import math
import random
import pygame

wn = turtle.Screen()
wn.title("Brickout")
wn.bgcolor("black")
wn.tracer(0)

stick = turtle.Turtle()
stick.speed(0)
stick.color("white")
stick.shape("square")
stick.shapesize(1,6)
stick.pu()
stick.sety(-250)

block1 = turtle.Turtle()
block1.speed(0)
block1.color("red")
block1.shape("square")
block1.shapesize(1.3, 3.5)
block1.pu()
block1.goto(-220,250)

block2 = turtle.Turtle()
block2.speed(0)
block2.color("red")
block2.shape("square")
block2.shapesize(1.3, 3.5)
block2.pu()
block2.goto(-120, 250)

block3 = turtle.Turtle()
block3.speed(0)
block3.color("red")
block3.shape("square")
block3.shapesize(1.3, 3.5)
block3.pu()
block3.goto(-20, 250)

block4 = turtle.Turtle()
block4.speed(0)
block4.color("red")
block4.shape("square")
block4.shapesize(1.3, 3.5)
block4.pu()
block4.goto(80, 250)

block5 = turtle.Turtle()
block5.speed(0)
block5.color("red")
block5.shape("square")
block5.shapesize(1.3, 3.5)
block5.pu()
block5.goto(180, 250)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.pu()
ball.sety(-230)
i=0
ball.dx=0.07
ball.dy=0.09

def stick_right():
    x=stick.xcor()
    x+=20
    stick.setx(x)
def stick_left():
    x = stick.xcor()
    x -= 20
    stick.setx(x)
wn.listen()
wn.onkeypress(stick_right,"Right")
wn.onkeypress(stick_left,"Left")

#Main game loop
while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)

    ball.sety(ball.ycor()+ball.dy)
             
    if ball.ycor()>=250:
        ball.sety(250)
        ball.dy -= 0.09
    elif ball.ycor()<=-250:
        ball.sety(-250)
        ball.dy = 0
        ball.dx = 0
        wn.bye()
    if ball.xcor()>=300:
        ball.setx(300)
        ball.dx -= 0.07
    elif ball.xcor()<=-300:
        ball.setx(-300)
        ball.dx +=0.07
       

    
    

