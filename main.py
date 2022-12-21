import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

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

# scoreboard setup
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < - 320 :
        ball.bounce_x()
    if ball.xcor() > 400:
        scoreboard.increase_score_left()
        ball.reset_position()
    if ball.xcor() < -400:
        scoreboard.increase_score_right()
        ball.reset_position()

screen.exitonclick()