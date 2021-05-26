from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("slowest")
        self.angle = 45
        self.setheading(self.angle)

    def restart(self):
        if self.heading() < 90 or self.heading() > 270:
            self.setheading(225)
        else:
            self.setheading(45)
        self.goto(0, 0)

