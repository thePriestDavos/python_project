from turtle import Turtle
FONT=('Arial',9,"bold")

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.color("white")
        self.hideturtle()
        self.score=0
        self.penup()
        self.goto(0,280)
        self.write("Score : "+str(self.score),False, align="center" ,font=FONT)  
        
    def inc_score(self):
        self.clear()
        self.score+=1
        self.write("Score : "+str(self.score),False, align="center" ,font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",False, align="center" ,font=('Arial',29,"bold"))
        
       