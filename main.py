from turtle import Screen
from classes.hirts_painter import hirts_painter

screen = Screen()
screen.colormode(255)

hirts = hirts_painter("image.png")
hirts.paint()
screen.exitonclick()