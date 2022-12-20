from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1,1)
        self.color("white")

    def move(self):
        new_x = self.xcor() + 0.05
        new_y = self.ycor() + 0.05
        self.goto(new_x, new_y)
