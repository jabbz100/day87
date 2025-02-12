from player_paddle import PlayerPaddle
from game_blocks import GameBlocks
from ball_object import Ball
from scoreboard import Scoreboard
from turtle import Screen
import time

screen = Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)

score = Scoreboard()

paddle_position = (0, -270)
paddle = PlayerPaddle(paddle_position)
screen.onkeypress(key="a", fun=paddle.move_left)
screen.onkeypress(key="d", fun=paddle.move_right)

ball = Ball()

blocks = GameBlocks()

game_on = True
while game_on:
    screen.update()

    blocks.spawn_bricks(ball, paddle, paddle_position)

    if ball.movement(paddle, paddle_position):
        score.lives -= 1
        score.draw_board()
    if score.lives == 0:
        score.game_over()
        break
    if blocks.game_logic(ball):
        score.score += 1
        score.draw_board()

    time.sleep(0.01)

screen.mainloop()
