from turtle import Turtle


class PlayerPaddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=0.7, stretch_len=7)
        self.paddle_reset(coordinates)

    def move_left(self):
        new_x = self.xcor() - 60
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 60
        self.goto(new_x, self.ycor())

    def paddle_reset(self, coordinates):
        self.goto(coordinates)
