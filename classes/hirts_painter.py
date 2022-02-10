from turtle import Turtle
from functions.color_pallete_generator import generate_colors
from random import choice

class hirts_painter:
    def __init__(self, color_pallete):
        self.hirts = Turtle(shape='turtle')
        self.hirts.penup()
        self.hirts.hideturtle()
        self.x_axis = -350
        self.y_axis = -320
        self.grid = 15 * 15
        self.hirts.goto(self.x_axis, self.y_axis)
        self.colors = generate_colors(color_pallete)

    def paint(self):
        for _ in range(1, self.grid):
            self.dot_generator()
            if _ % 15 == 0:
                self.x_axis = -350
                self.y_axis += 50
                self.hirts.goto(self.x_axis, self.y_axis)
            
    
    def dot_generator(self):
        self.hirts.dot(20, choice(self.colors))
        self.hirts.fd(50)



