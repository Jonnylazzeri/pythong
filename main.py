from turtle import Screen
from line import Line
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
line = Line()
line.move_turtle()

right_paddle = Paddle()
left_paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

ball_speed = 0.1

right_paddle.set_position((350, 0))
left_paddle.set_position((-350, 0))

screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 325 or ball.distance(left_paddle) < 50 and ball.xcor() < -325:
        ball_speed -= 0.005
        if ball_speed < 0:
            ball_speed = 0
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.left_score += 1
        scoreboard.update_score()
        ball.goto(0, 0)
        ball.x_move = -10
        ball.y_move = -10
        ball_speed = 0.1

    if ball.xcor() < -390:
        scoreboard.right_score += 1
        scoreboard.update_score()
        ball.goto(0, 0)
        ball.x_move = 10
        ball.y_move = 10
        ball_speed = 0.1



screen.exitonclick()
