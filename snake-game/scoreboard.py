from turtle import Turtle
from snake import Snake

ALIGNMENT = 'center'
FONT = ('Courier',14,'normal')
class ScoreBoard(Turtle,Snake):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.write(f'SCORE: {self.score}',align=ALIGNMENT,font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f'SCORE: {self.score } HIGH SCORE: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()



    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER',align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()


