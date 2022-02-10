from turtle import Turtle
from random import  choice
from functions.change_color import change_color
class ShapeDrawer:
    def __init__(self, shapes):
        self.shape = shapes
        self.tim = Turtle(shape='turtle')
        self.tim.color('goldenrod')
        self.color = ''

    def draw(self, sides):
        for _ in range(sides):
            self.tim.forward(100)
            self.tim.right(360/sides)
    
    # def change_color(self):
    #     self.color = ["#"+''.join([choice('ABCDEF0123456789') for i in range(6)])]
    #     self.tim.color(self.color)
        

    def draw_shapes(self):
        for shape in self.shape:
            self.tim.color(change_color())
            if shape == 'triangle':
                self.draw(sides=3)
            elif shape == 'square':
                self.draw(sides=4)
            elif shape == 'pentagon':
                self.draw(sides=5)
            elif shape == 'hexagon':
                self.draw(sides=6)
            elif shape == 'heptagon':
                self.draw(sides=7)
            elif shape =='nonagon':
                self.draw(sides=8)
            elif shape =='decagon':
                self.draw(sides=9)

   

