from turtle import Turtle, Screen
from random import randint
from functions.inputCheck import inputCheck

x = -240
y = -100
screen = Screen()
screen.setup(width=500, height=400)
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
bet_question = "Which turtle will win the race? Enter the colour of the turtle"
turtles = []
race = False


for turtle in range(len(colours)):
    turtles.append(Turtle(shape='turtle'))
    turtles[turtle].color(colours[turtle])
    turtles[turtle].penup()
    turtles[turtle].goto(x, y)
    y = y + 50


user_bet = screen.textinput("Make your bet!", f"{bet_question}").lower()

while inputCheck(user_bet, colours) == False:
    user_bet = screen.textinput("Inccorect colour", f"Please remake your bet, {bet_question}")
    race = inputCheck(user_bet, colours)

while race:
    for turtle in turtles:
        random_distance = randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            race = False
            if turtle.pencolor() == user_bet:
                print(f"You've won, the winning colour is {turtle.pencolor()}")
            
            else:
                print(f"You've lost, the winning colour is {turtle.pencolor()}")
            
            #screen.bye()

screen.exitonclick()
