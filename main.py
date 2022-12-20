from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

# Screen setup
screen_width = 800
screen_height = 600

screen = Screen()
screen.bgcolor("black")
screen.setup(screen_width, screen_height)
screen.title("Pong")
screen.tracer(0)

# Paddles setup
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# Paddles movement
screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

# Ball setup
ball = Ball()


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

screen.exitonclick()