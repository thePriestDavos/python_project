from turtle import Screen
from snake import Snake as s
from food import Food , food2
from scoreboard import scoreboard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=s()
food=food2()
sb=scoreboard()

screen.listen()
screen.onkey(key="Up" ,fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,key="Right")

     
gameis_on=True
while gameis_on:
    screen.update()
    time.sleep(.1)  
                          
    snake.move() 
    
    #Detect collision with food
    # print(snake.all_segments[0].position())
    # print(food.dis)
    # if snake.all_segments[0].distance(food)<17:
    #     food.refresh()
    if snake.all_segments[0].distance(food.dis)<17:
        food.refresh() 
        sb.inc_score()
        snake.extend()
    
    #Detect collison with wall
    if snake.all_segments[0].xcor()>280 or snake.all_segments[0].xcor()<-280 or snake.all_segments[0].ycor()>280 or snake.all_segments[0].ycor()<-280:
        gameis_on=False
        sb.game_over()
    
    #Detect collison with tail
    for segment in snake.all_segments[1:]:
        if  snake.all_segments[0].distance(segment)<10:
            sb.game_over()
            gameis_on=False
        
    
        
screen.exitonclick()
