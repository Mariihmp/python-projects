import turtle as t
import  time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
tr = t.Turtle()
scr = t.Screen()
scoreb = ScoreBoard()

scr.setup(width=600,height=600)
scr.bgcolor('black')
scr.title('THE SNAKE GAME')
scr.tracer(0)

snake = Snake()
food = Food()


scr.listen()
scr.onkey(snake.up,'Up')
scr.onkey(snake.down,'Down')
scr.onkey(snake.left,'Left')
scr.onkey(snake.right,'Right')


#TODO: snake body is 3 square
#TODO:move snake automatically we shhould change the direction

game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)< 20:
        food.refresh()
        snake.extend()
        scoreb.increase_score()
        #detect collision

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor() <-280:
        game_is_on = False
        scoreb.game_over()




#TODO: Detection collision with foodv
#TODO: creat a scoreboardv
#TODO: detect collison with wall v



#TODO: detect collision with tail X
#if head colides with any segment  in the tail :
    #trigger the game over

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            scoreb.game_over()

scr.exitonclick()