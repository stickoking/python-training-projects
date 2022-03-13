from turtle import Turtle, Screen
from classes.snake import Snake
from classes.food import Food
from classes.scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
initial_length = 3
game_is_on = True

snake = Snake()
food = Food()
score_board = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_generator()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.tally_score()
    
    #Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < (-285) or snake.head.ycor() > 285 or snake.head.ycor() < (-285):
        game_is_on = False
        score_board.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
             game_is_on = False
             score_board.game_over()


    

screen.exitonclick()