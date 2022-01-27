from turtle import Turtle

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 600
X_POS_PLAYER_1 = -40
X_POS_PLAYER_2 = 40
Y_POS_PLAYER = int(SCREEN_HEIGHT / 2) - 50
ALIGN = 'center'
FONT = 'Times'
FONT_SIZE = 30
FONT_TYPE = 'bold'

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.score = 0



    def player_1(self):
        self.goto(x=X_POS_PLAYER_1, y=Y_POS_PLAYER)
        self.clear()
        self.write(self.score, align=ALIGN, font=(FONT, FONT_SIZE, FONT_TYPE))


    def player_2(self):
        self.goto(x=X_POS_PLAYER_2, y=Y_POS_PLAYER)
        self.clear()
        self.write(self.score, align=ALIGN, font=(FONT, FONT_SIZE, FONT_TYPE))


    def increase(self):
        self.score += 1
