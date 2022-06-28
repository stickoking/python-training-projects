import pandas
from turtle import Turtle


class StateChecker:

    def __init__(self, screens):
        self.data = pandas.read_csv("50_states.csv")
        self.prompt = ""
        self.answer = ""
        self.screen = screens
        self.totalData = self.data.state.size
        self.score = 0
        self.prompts = "What's another state name?"
        self.title = "Guess the State"
        self.turtle = Turtle(shape='turtle')
        self.turtle.penup()
        self.turtle.hideturtle()
        self.x_axis = 0
        self.y_axis = 0

    def set_state_title(self):
        self.title = f"{self.score}/{self.totalData} States Correct'"
        self.prompt_user()

    def prompt_user(self):
        self.prompt = self.screen.textinput(title=self.title, prompt=self.prompts)
        self.verify()

    def verify(self):
        self.answer = self.data[self.data.state.str.lower() == self.prompt.lower()]
        if self.answer.empty:
            self.set_state_title()
        else:
            self.score += 1
            self.x_axis = int(self.answer.x)
            self.y_axis = int(self.answer.y)
            self.turtle.goto(self.x_axis, self.y_axis)
            self.turtle.write(self.answer.state.to_numpy()[0], True, align="center")
            if self.score < self.totalData:
                self.set_state_title()
            else:
                self.x_axis = 0
                self.x_axis = 0
                self.turtle.goto(self.x_axis, self.y_axis)
                self.turtle.write("You Win", True, align="center", font=('Arial', 30, 'bold'))
