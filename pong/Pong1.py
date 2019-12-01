# Simple Pong
# base on TokyoEdTech
# https://www.christianthompson.com
import turtle
import os #winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A - Paleta A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed of animation
paddle_a.shape("square") # hay otras formas
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # por defecto es 20x20 pixeles la forma.
paddle_a.penup()
paddle_a.goto(-350,0) # 0,0 es el medio.

# Paddle B - Paleta B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # speed of animation
paddle_b.shape("square") # hay otras formas
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # por defecto es 20x20 pixeles la forma.
paddle_b.penup()
paddle_b.goto(350,0) # 0,0 es el medio.

# Ball - Bola
ball = turtle.Turtle()
ball.speed(0) # speed of animation
ball.shape("square") # hay otras formas
ball.color("white")
ball.penup()
ball.goto(0,0) # 0,0 es el medio.
ball.dx = 1.25
ball.dy = 1.25

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Plaber B: 0", align="center", font=("Courier", 24, "normal"))

# Funtion
def paddle_a_up():
  y = paddle_a.ycor()
  y += 20
  paddle_a.sety(y)

def paddle_a_down():
  y = paddle_a.ycor()
  y -= 20
  paddle_a.sety(y)

def paddle_b_up():
  y = paddle_b.ycor()
  y += 20
  paddle_b.sety(y)

def paddle_b_down():
  y = paddle_b.ycor()
  y -= 20
  paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkey(paddle_a_up, "w") # onkey or onkeypress depende de la version de python
wn.onkey(paddle_a_down, "s")
wn.onkey(paddle_b_up, "Up")
wn.onkey(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
      ball.sety(290)
      ball.dy *= -1
      os.system("aplay bounce.wav&") #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
      ball.sety(-290)
      ball.dy *= -1
      os.system("aplay bounce.wav&")

    if ball.xcor() > 390:
      ball.goto(0,0)
      ball.dx *= -1
      score_a +=1
      pen.clear()
      pen.write("Player A: {} Plaber B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
      ball.goto(0,0)
      ball.dx *= -1
      score_b += 1

    # Compare Paddle with Ball - collitions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50 ):
      ball.setx(340)
      ball.dx *= -1
      os.system("aplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50 ):
      ball.setx(-340)
      ball.dx *= -1
      os.system("aplay bounce.wav&")
