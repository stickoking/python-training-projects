from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode = "r") as data:
            self.highscore = int(data.read())
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            with open("data.txt", mode = "w") as data:
                self.highscore = self.score
                data.write(f"{self.highscore}")
        self.score = 0
        self.write_score()

    def tally_score(self):
        self.score += 1
        self.write_score()