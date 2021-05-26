from turtle import Turtle


ALIGN = "center"
FONT = ("Arial", 30, "normal")


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.pensize(20)
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write(self.score, align=ALIGN, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write(self.score, align=ALIGN, font=FONT)

