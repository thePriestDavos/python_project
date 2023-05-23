from turtle import Turtle 
import random

X=20
MOVE_DIST=15

COLOR=["red","red", "green", "blue","white","indigo", "green", "blue","white","indigo","red", "green", "blue","white","indigo","red", "green", "blue","white","indigo","red", "green", "blue","white","indigo","red", "green", "blue","white","indigo" ]
STARTING_pOSITION=[(0,0),(-20,0),(-41,0)]
class Snake:
    def __init__(self):   
        self.all_segments=[] 
        self.create_snake()
        self.create_boundary()
    def create_snake(self):
        # for i in range(3):
        #     self.add_segment(X)
        for position in STARTING_pOSITION:
            self.add_segment(position)
            
    def add_segment(self,positions):
        new_segment=Turtle(shape="square")
        new_segment.penup()
        new_segment.color(random.choice(COLOR))
        # x=X-20
        # new_segment.setx(new_segment.xcor()+x)
        new_segment.goto(positions)
        self.all_segments.append(new_segment)
    
    def extend(self):
        self.add_segment(self.all_segments[-1].position())
        
    def move(self):
        for i in range(len(self.all_segments)-1,0,-1):#3
            new_x=self.all_segments[i-1].xcor()
            new_y=self.all_segments[i-1].ycor()
            self.all_segments[i].goto(new_x,new_y) 
        self.all_segments[0].forward(MOVE_DIST)
        
        # self.all_segments[0].right(180)
        
    
    # def up(self):
    #     self.all_segments[0].setheading(90)
    # def down(self):
    #     self.all_segments[0].setheading(270)
    # def left(self):
    #     self.all_segments[0].setheading(180)   
    # def right(self):
    #     self.all_segments[0].setheading(0)
        
    def up(self):
        if self.all_segments[0].heading() != 270:
            self.all_segments[0].setheading(90)
    def down(self):
        if self.all_segments[0].heading() != 90:
            self.all_segments[0].setheading(270)
    def left(self):
        if self.all_segments[0].heading() != 0:
            self.all_segments[0].setheading(180)   
    def right(self):
        if self.all_segments[0].heading() != 180:
            self.all_segments[0].setheading(0)   
            
    
            
    def create_boundary(self) :
        self.t=Turtle()
        self.t.color("red")
        self.t.hideturtle()
        self.t.penup()
        self.t.goto(-280,280)
        self.t.pendown()
        self.t.forward(560)
        for i in range(3): 
            self.t.right(90)
            self.t.forward(560)
       
         
         
    