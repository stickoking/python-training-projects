import turtle
from classes.state_checker import StateChecker
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

stateChecker = StateChecker(screen)
stateChecker.prompt_user()

screen.exitonclick()