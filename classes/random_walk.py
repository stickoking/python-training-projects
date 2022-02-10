from turtle import Turtle
from random import choice
import turtle
from functions.change_color import change_color

turtle.colormode(255)

class RandomWalk:
    def __init__(self):
        
        self.direction_angels = [0, 90, 180, 270]
        self.tim = Turtle(shape="turtle")
        self.tim.color(change_color())
        self.tim.pensize(10)
        self.tim.speed("fastest")

    def walk(self):
        while True:
            self.tim.forward(25)
            self.tim.setheading(choice(self.direction_angels))
            self.tim.color(change_color())



