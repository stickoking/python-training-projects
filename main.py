from turtle import Turtle, Screen

tim = Turtle(shape='turtle')
tim.penup()
tim.goto(-240, -100)
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet!", "Which turtle will win the race? Enter the colour of the turtle")
print(user_bet)


screen.exitonclick()
