from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.goto(0, -285)
        self.left(90)

    def move_turtle(self):
        self.width(3)

        while self.ycor() < 290:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
            self.hideturtle()

