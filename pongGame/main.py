#TODO:'''
# creat the screen
# creat and move paddle
# creat another paddle
# creat the ball and make it move
# detect collision with wall and bounce
# detect collision with paddle
# detect when paddle misses
# keep score '''
import turtle as t
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


scr = t.Screen()
#move with w and s keyword
scoreboard = Scoreboard()

scr.setup(width=800,height=600)
scr.bgcolor('black')
scr.title('PONG')
scr.tracer(0)
scr.listen()

paddleRight = Paddle((350,0))
paddleLeft = Paddle((-350,0))
ball = Ball()
#MAKing paddle
#width 20 , height 100
#x_pos 350,,, y_pos = 0
scr.onkey(paddleRight.move_up,'Up')
scr.onkey(paddleRight.move_down,'Down')

scr.onkey(paddleLeft.move_up,'w')
scr.onkey(paddleLeft.move_down,'s')

game_is_on = True
starting_time = 0.1
while game_is_on:
    time.sleep(ball.move_speed)
    scr.update()
    ball.move()
    if ball.ycor()> 280 or ball.ycor()<-300:
        ball.bounce_y()

    if ball.distance(paddleRight) <50 and ball.xcor()> 320 or ball.distance(paddleLeft) < 50 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.xcor() >380:
        ball.reset_position()
        scoreboard.l_point()


    if ball.xcor()< -380:
        ball.reset_position()
        scoreboard.r_point()





'''detect collision with pedal 
'''


scr.exitonclick()
