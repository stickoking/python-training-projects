from ast import IsNot
from random import randint
from re import X
from turtle import Screen, xcor
from classes.paddle import Paddle
from classes.ball import Ball
import time


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
UP = 90
DOWN = 270
UPPER_BOUND = 300
LOWER_BOUND = -300

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width= SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
game_is_on = True


computer_paddle = Paddle(-((SCREEN_WIDTH/2) - 20), screen, UP)
player_paddle = Paddle((SCREEN_WIDTH/2) - 30, screen, UP)
ball = Ball()
#screen.update()
screen.listen()


screen.onkey(player_paddle.up, "w")
screen.onkey(player_paddle.down, "s")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    computer_paddle.auto_move()
    ball.move_ball()
    
    #Move Computer paddle and check for collistion with bottom & top wall
    if computer_paddle.paddle.ycor() > UPPER_BOUND - 75:
        computer_paddle.paddle.setheading(DOWN)
    if computer_paddle.paddle.ycor() < LOWER_BOUND + 65:
        computer_paddle.paddle.setheading(UP)
    
    #Check collision of player paddle with bottom & top wall
    if player_paddle.paddle.ycor() <= UPPER_BOUND:
        screen.onkey(player_paddle.up, "Up")
        #player_paddle.paddle.setposition(-((SCREEN_WIDTH/2) - 20), UPPER_BOUND + 25)
    if player_paddle.paddle.ycor() >= LOWER_BOUND:
        screen.onkey(player_paddle.down, "Down")
        #player_paddle.paddle.setposition(-((SCREEN_WIDTH/2) - 20), LOWER_BOUND - 15)
    if ball.ycor() >= UPPER_BOUND - 15 or ball.ycor() <= LOWER_BOUND + 15:
        ball.bounce_y()
    
    if ball.distance(computer_paddle.paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()
        
    
    

screen.exitonclick()