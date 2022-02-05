from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')
tim.color('goldenrod')

sides = 4

for _ in range(sides):
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()
