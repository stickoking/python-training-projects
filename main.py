from turtle import Screen, Turtle
import turtle
from classes.shape_drawer import ShapeDrawer;
from classes.random_walk import RandomWalk
from classes.spirograph import Spirograph
import heroes 
SIZE = 20
print(heroes.gen())

# tim = Turtle(shape='turtle', visible=False)
# tim.color('goldenrod')
screen = Screen()
# tim.penup()
# tim.goto(SIZE/2 - screen.window_width()/2, 0)
# tim.pendown()
# tim.showturtle()

# sides = 4

# for _ in range(sides):
#     tim.forward(100)
#     tim.right(90)

# gap = 10

# def up(gap):
#     tim.pendown()
#     tim.forward(gap)

# def down(gap):
#     tim.penup()
#     tim.forward(gap)


# for _ in range(25):
#     up(gap)
#     down(gap)
# shapes =["triangle", "square", "pentagon", "octagon", "hexagon", "heptagon", "nonagon", "decagon"]

# tim_shaper = ShapeDrawer(shapes=shapes)
# tim_shaper.draw_shapes()

# tim_walker = RandomWalk()
# tim_walker.walk()

tim_spirograpth = Spirograph()
tim_spirograpth.draw()

screen.exitonclick()


