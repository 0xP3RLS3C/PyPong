from turtle import Turtle

ALLIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_right = 0
        self.score_left = 0
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.write(f"{self.score_left} : {self.score_right}", align=ALLIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score_right(self):
        self.clear()
        self.score_right += 1
        self.write(f"{self.score_left} : {self.score_right}", align=ALLIGNMENT, font=FONT)

    def increase_score_left(self):
        self.clear()
        self.score_left += 1
        self.write(f"{self.score_left} : {self.score_right}", align=ALLIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align=ALLIGNMENT, font=FONT)