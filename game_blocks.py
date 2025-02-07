from turtle import *
from random import choice
from time import sleep

COLORS = ["red", "green", "yellow", "purple", "orange",
          "pink", "cyan", "lime", "violet", "gold"]


class GameBlocks:
    def __init__(self):
        self.block_list = []
        self.start_x = -360
        self.start_y = 240
        self.block_width = 65
        self.block_height = 30

    def spawn_bricks(self, ball, paddle, coordinates):
        if not self.block_list:
            ball.ball_reset()
            paddle.paddle_reset(coordinates)
            for row in range(4):
                for col in range(12):
                    block = Turtle()
                    block.shapesize(stretch_wid=1, stretch_len=2.7)
                    block.shape("square")
                    block.penup()

                    # block.color(choice(COLORS))
                    if row <= 1:
                        block.color("purple")
                    else:
                        block.color("green")
                    block.goto(self.start_x + col * self.block_width, self.start_y - row * self.block_height)
                    self.block_list.append(block)
            sleep(1.5)

    def game_logic(self, ball):
        for block in self.block_list[:]:  # Iterate over a copy to avoid modifying the list during iteration
            if (
                    block.xcor() - 30 <= ball.xcor() <= block.xcor() + 30
                    and block.ycor() - 15 <= ball.ycor() <= block.ycor() + 15
            ):
                block.hideturtle()
                self.block_list.remove(block)

                if abs(ball.ycor() - block.ycor()) <= 20:
                    ball.y *= -1
                else:
                    ball.x *= -1

                return True
        return False
