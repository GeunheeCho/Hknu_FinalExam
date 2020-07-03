import turtle
import pygame
import pygame.mixer as sounds
sounds.init()

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

def stick_right():
    x = stick.xcor()
    x += 20
    stick.setx(x)

def stick_left():
    x = stick.xcor()
    x -= 20
    stick.setx(x)

wn.listen()
wn.onkeypress(stick_right, "Right")
wn.onkeypress(stick_left, "Left")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.pu()
ball.sety(-230)
ball.dx = 0.2
ball.dy = 0.4

#block1
b1 = turtle.Turtle()
b1.speed(0)
b1.color("red")
b1.shape("square")
b1.shapesize(1.3, 3.5)
b1.pu()
b1.goto(-180, 250)
#block2
b2 = turtle.Turtle()
b2.speed(0)
b2.color("red")
b2.shape("square")
b2.shapesize(1.3, 3.5)
b2.pu()
b2.goto(-50, 250)
#block3
b3 = turtle.Turtle()
b3.speed(0)
b3.color("red")
b3.shape("square")
b3.shapesize(1.3, 3.5)
b3.pu()
b3.goto(80, 250)
#block4
b4 = turtle.Turtle()
b4.speed(0)
b4.color("red")
b4.shape("square")
b4.shapesize(1.3, 3.5)
b4.pu()
b4.goto(210, 250)
#block5
b5 = turtle.Turtle()
b5.speed(0)
b5.color("yellow")
b5.shape("square")
b5.shapesize(1.3, 3.5)
b5.pu()
b5.goto(-180, 200)
#block6
b6 = turtle.Turtle()
b6.speed(0)
b6.color("yellow")
b6.shape("square")
b6.shapesize(1.3, 3.5)
b6.pu()
b6.goto(-50, 200)
#block7
b7 = turtle.Turtle()
b7.speed(0)
b7.color("yellow")
b7.shape("square")
b7.shapesize(1.3, 3.5)
b7.pu()
b7.goto(80, 200)
#block8
b8 = turtle.Turtle()
b8.speed(0)
b8.color("yellow")
b8.shape("square")
b8.shapesize(1.3, 3.5)
b8.pu()
b8.goto(210, 200)
#게임실행
while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #벽에 부딪히는 거         
    if ball.ycor()>=250:
        ball.sety(250)
        ball.dy *= -1 
    elif ball.ycor()<=-250:
        ball.sety(-250)
        ball.dy = 0
        ball.dx = 0
    if ball.xcor()>=300:
        ball.setx(300)
        ball.dx *= -1
    elif ball.xcor()<=-300:
        ball.setx(-300)
        ball.dx *= -1
        #막대에 부딪히는거
    if ball.ycor() < -230 and (ball.xcor() < stick.xcor()+60 and ball.xcor() > stick.xcor()-60):
        ball.dy *= -1 
        #벽돌에 ~
    if (ball.ycor() < b1.ycor()+13 and ball.ycor() > b1.ycor()-13) and (ball.xcor() < b1.xcor()+35 and ball.xcor() > b1.xcor()-35):
        ball.dy *= -1
        b1.goto(900, 900)
    if (ball.ycor() < b2.ycor()+13 and ball.ycor() > b2.ycor()-13) and (ball.xcor() < b2.xcor()+35 and ball.xcor() > b2.xcor()-35):
        ball.dy *= -1
        b2.goto(900, 900)
    if (ball.ycor() < b3.ycor()+13 and ball.ycor() > b3.ycor()-13) and (ball.xcor() < b3.xcor()+35 and ball.xcor() > b3.xcor()-35):
        ball.dy *= -1
        b3.goto(900, 900)
    if (ball.ycor() < b4.ycor()+13 and ball.ycor() > b4.ycor()-13) and (ball.xcor() < b4.xcor()+35 and ball.xcor() > b4.xcor()-35):
        ball.dy *= -1
        b4.goto(900, 900)
    if (ball.ycor() < b5.ycor()+13 and ball.ycor() > b5.ycor()-13) and (ball.xcor() < b5.xcor()+35 and ball.xcor() > b5.xcor()-35):
        ball.dy *= -1
        b5.goto(900, 900)
    if (ball.ycor() < b6.ycor()+13 and ball.ycor() > b6.ycor()-13) and (ball.xcor() < b6.xcor()+35 and ball.xcor() > b6.xcor()-35):
        ball.dy *= -1
        b6.goto(900, 900)
    if (ball.ycor() < b7.ycor()+13 and ball.ycor() > b7.ycor()-13) and (ball.xcor() < b7.xcor()+35 and ball.xcor() > b7.xcor()-35):
        ball.dy *= -1
        b7.goto(900, 900)
    if (ball.ycor() < b8.ycor()+13 and ball.ycor() > b8.ycor()-13) and (ball.xcor() < b8.xcor()+35 and ball.xcor() > b8.xcor()-35):
        ball.dy *= -1
        b8.goto(900, 900)

    