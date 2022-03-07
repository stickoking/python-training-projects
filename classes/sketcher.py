from turtle import Turtle, Screen

class sketcher:
    def __init__(self):
        self.tim = Turtle()
        self.Screen = Screen()
        
    def w(self):
        self.tim.forward(10)
    
    def s(self):
        self.tim.back(10)
    
    def a(self):
        self.tim.left(10)
    
    def d(self):
        self.tim.right(10)
    
    def clear(self):
        self.tim.reset()

    
    def sketch(self):
        self.Screen.onkey(key='w', fun=self.w)
        self.Screen.onkey(key='s', fun=self.s)
        self.Screen.onkey(key='a', fun=self.a)
        self.Screen.onkey(key='d', fun=self.d)
        self.Screen.onkey(key='c', fun=self.clear)
        self.Screen.listen()
        self.Screen.exitonclick()
        


        