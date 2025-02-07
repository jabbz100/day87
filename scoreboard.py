from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard:
    def __init__(self):
        self.board = Turtle()
        self.board.hideturtle()
        self.board.penup()
        self.board.color("white")

        self.lives = 3
        self.score = 0

        self.draw_board()

    def draw_line(self):
        self.board.goto(-390, 260)
        self.board.pendown()
        self.board.goto(385, 260)
        self.board.penup()

    def draw_lives(self):
        self.board.goto(-200, 265)
        self.board.write(f"LIVES: {self.lives}", font=FONT)

    def draw_score(self):
        self.board.goto(-380, 265)
        self.board.write(f"SCORE: {self.score}", font=FONT)

    def draw_board(self):
        self.board.clear()
        self.draw_line()
        self.draw_score()
        self.draw_lives()

    def game_over(self):
        self.board.goto(0, 0)
        self.board.write("GAME OVER", font=FONT, align="center")
