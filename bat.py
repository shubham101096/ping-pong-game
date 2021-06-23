from turtle import Turtle




class Bat(Turtle):
    def __init__(self, position):
            super().__init__()
            self.shape("square")
            self.color("white")
            self.penup()
            self.shapesize(1, 5)
            self.goto(position)
            self.setheading(90)

    def head_down(self):
        if self.ycor() < -260:
            return
        self.setheading(270)
        self.forward(20)

    def head_up(self):
        if self.ycor() > 260:
            return
        self.setheading(90)
        self.forward(20)

    def move(self):
        if self.ycor() > 260:
            self.head_down()
        elif self.ycor() < -260:
            self.head_up()
        self.forward(10)

