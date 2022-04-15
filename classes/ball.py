from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        #self.p([-45, 45])
        #self.setheading(randint(45, 225))
        #self.move_ball() 
        self.y_move = 10
        self.x_move = 10
    
    def move_ball(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1