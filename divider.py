from turtle import Turtle


class Divider(Turtle):
    def __init__(self):
        super().__init__()
        divider = Turtle(shape="square")
        divider.color("white")
        divider.pensize(10)
        divider.penup()
        divider.hideturtle()
        divider.goto(0, -280)
        divider.setheading(90)
        for i in range(15):
            divider.pendown()
            divider.forward(20)
            divider.penup()
            divider.forward(20)




