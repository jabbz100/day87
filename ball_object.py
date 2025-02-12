from turtle import Turtle
from random import choice

BALL_SPEED = -5


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0, 0)

        self.x = choice([1, -1])
        self.y = BALL_SPEED

    def movement(self, paddle, paddle_coordinates):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)
        self.ball_bounce(paddle)
        if self.ycor() >= 350 or self.ycor() <= -350:
            self.ball_reset()
            paddle.goto(paddle_coordinates)
            return True
        return False

    def ball_bounce(self, paddle):
        if abs(self.xcor()) > 385:
            self.x *= -1
        if self.ycor() >= 248:
            self.y *= -1
        if self.distance(paddle) < 70 and -258 >= self.ycor() >= -280:
            offset = self.xcor() - paddle.xcor()
            self.x = max(min((offset / 35) * 3, 4), -3)
            self.y *= -1

    def ball_reset(self):
        self.goto(0, 0)
        self.x = choice([1, -1])
        self.y = BALL_SPEED

    