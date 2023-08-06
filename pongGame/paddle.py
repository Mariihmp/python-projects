from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,tpCoardinate):
        super().__init__()
        self.shape('square')
        self.shapesize(5, 1)
        self.color('white')
        self.penup()
        self.goto(tpCoardinate)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

