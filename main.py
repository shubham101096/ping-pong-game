from turtle import Turtle, Screen
from bat import Bat
import time
from divider import Divider
from ball import Ball
from score import Score

POSA = (-350, 0)
POSB = (350, 0)

SCORE_POSA = (-40, 260)
SCORE_POSB = (40, 260)

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")

game_is_on = True
bat_a = Bat(POSA)
bat_b = Bat(POSB)
divider = Divider()

ball = Ball()
score_a = Score(SCORE_POSA)
score_b = Score(SCORE_POSB)

screen.listen()
screen.onkey(bat_a.head_up, "w")
screen.onkey(bat_a.head_down, "s")
screen.onkey(bat_b.head_up, "Up")
screen.onkey(bat_b.head_down, "Down")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # bat_a.move()
    # bat_b.move()
    ball.forward(20)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.setheading(360-ball.heading())

    if ball.distance(bat_a.position()) < 50:
        ball.setheading(abs(80-ball.heading()))

    elif ball.distance(bat_b.position()) < 50:
        ball.setheading(abs(80 - ball.heading()))

    if ball.xcor() > 350:
        score_a.update()
        ball.restart()
    elif ball.xcor() < -350:
        score_b.update()
        ball.restart()


screen.exitonclick()