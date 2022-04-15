from turtle import Turtle
import time

MOVE_DISTANCE = 20
class Paddle:
    def __init__(self, start_position, screen, up):
        super().__init__()
        self.screen = screen
        self.starting_position = (start_position, 0)
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.setheading(up)
        self.paddle.shapesize(stretch_len=5, stretch_wid=1)
        self.paddle.goto(self.starting_position)
                
    def auto_move(self):
        
        self.paddle.forward(MOVE_DISTANCE)
        self.screen.update()
    
    def up(self):
        time.sleep(0.1)
        self.paddle.forward(MOVE_DISTANCE)
        self.screen.update()
        
        
        

    def down(self):
        time.sleep(0.1)
        self.paddle.backward(MOVE_DISTANCE)
        self.screen.update()
