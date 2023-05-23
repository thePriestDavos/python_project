from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5 ,stretch_wid=0.5)
        self.color("green")
        self.speed(0)
        self.refresh()
    def refresh(self):
        x=random.randint(-270,270)
        y=random.randint(-270,270)
        self.goto(x,y)
        
 
class food2():
    def __init__(self):
        self.food=Turtle(shape="circle")
        self.food.penup()
        self.food.shapesize(stretch_len=0.5 ,stretch_wid=0.5)
        self.food.color("green")
        self.food.speed(0)
        self.dis=self.refresh()
       
    def refresh(self):
        x=random.randint(-270,270)
        y=random.randint(-270,270)
        self.food.goto(x,y)
        self.dis=self.food.position()
        return self.dis
        
        
        
           