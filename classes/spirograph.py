from turtle import Turtle
from functions.change_color import change_color

class Spirograph:
    def __init__(self):
        self.tim = Turtle(shape='turtle')
        self.angle = 0
        self.tim.speed('fast')

    def draw(self):
        for _ in range(36):
            self.draw_spirograph()
            self.angle += 10

    def draw_spirograph(self):
        self.tim.color(change_color())
        self.tim.tilt(self.angle)
        self.tim.circle(100)
        self.tim.left(10)
        
        
