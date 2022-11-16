import turtle
import os

wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

score_a=0
score_b=0

# Paddle Player A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle Player B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=2
ball.dy=2

# Functions
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("plyr A = "+ str(score_a)+    "  plyr B = " + str(score_b), align="center", font=("Courier", 24))

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

# Main game loop
while True:
    wn.update()
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1
        os.system("afplay boing-6222.mp3&")

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *=-1
        os.system("afplay boing-6222.mp3&")

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a+=1
        pen.clear()
        #pen.write("player a has scored",align="right", font=("Courier", 24))
        pen.write("Player A = " + str(score_a) + "    Player B = " + str(score_b), align="center", font=("Courier", 24))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *=-1
        score_b+=1
        pen.clear()
        #pen.write("player b has scored", align="left", font=("Courier", 24))
        pen.write("Player A = " + str(score_a) + "    Player B = " + str(score_b), align="center", font=("Courier", 24))

    # Paddle ball collisions

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor() < paddle_b.ycor() +50) and (ball.ycor() > paddle_b.ycor()-50):
        ball.dx *=-1
        os.system("afplay boing-6222.mp3&")

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor() < paddle_a.ycor() +50) and (ball.ycor() > paddle_a.ycor()-50):
        ball.dx *=-1
        os.system("afplay boing-6222.mp3&")