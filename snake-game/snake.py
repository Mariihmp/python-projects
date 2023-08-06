from turtle import Turtle,Screen
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    scr = Screen()

    def __init__(self):
        self.segments =[]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_segment(i)


    def add_segment(self,position):
        sq = Turtle('square')
        sq.color('dark green')
        sq.penup()
        sq.goto(position)
        self.segments.append(sq)
    def extend(self):
        #add a new segment to the snake
        self.add_segment(self.segments[-1].position())


    #TODO:move snake automatically we shhould change the direction
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() !='DOWN':
            self.head.setheading(UP)
        #set heading to
    #when it goes up means (x,y)
    #snake moves to (x,y+20)


    def down(self):
        if self.head.heading() !='DOWN':
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() !='LEFT':
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() !='DOWN':
            self.head.setheading(RIGHT)
