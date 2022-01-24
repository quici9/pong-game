from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time, random

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 600


def detect_collision_wall(direction):
    '''
    Detect ball collision with wall.
    '''
    if int(ball.ycor()) == 190:
        if direction == 45:
            ball.setheading(315)
        elif direction == 135:
            ball.setheading(225)
    elif int(ball.ycor()) == -190:
        if direction == 315:
            ball.setheading(45)
        elif direction == 225:
            ball.setheading(135)


def detect_collision_player_1(direction):
    '''
    Detect ball collision with paddle of player 1.
    '''
    for segment in player_1.segments:
        if ball.distance(segment) < 20:
            if direction == 225:
                ball.setheading(315)
            elif direction == 135:
                ball.setheading(45)


def detect_collision_player_2(direction):
    '''
    Detect ball collision with paddle of player 2.
    '''
    for segment in player_2.segments:
        if ball.distance(segment) < 20:
            if direction == 45:
                ball.setheading(135)
            elif direction == 315:
                ball.setheading(225)


def game_over():
    '''
    Return True if detect when paddle misses. Otherwise, return False.
    Increase score for winner.
    '''
    if ball.xcor() > (SCREEN_WIDTH / 2 + 10):#Player 2 miss.
        score_player_1.increase()
        return True
    elif ball.xcor() < -(SCREEN_WIDTH / 2 + 10):#Player 1 miss.
        score_player_2.increase()
        return True
    else:
        return False


def game_start():
    '''
    Generate game from in the beginning (player, ball, score).
    '''
    player_1.player_1_start()
    player_2.player_2_start()
    score_player_1.player_1()
    score_player_2.player_2()
    ball.start_game()


def create_br():
    '''
    Create line center.
    '''
    line = Turtle()
    line.hideturtle()
    line.color('white')
    line.pensize(2)
    line.penup()
    line.goto(0, -190)
    line.setheading(90)
    while line.ycor() < 190:
        line.forward(10)
        line.pendown()
        line.forward(10)
        line.penup()



#Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
create_br()

#Generate player, ball, and score.
player_1 = Paddle()
player_2 = Paddle()
score_player_1 = Score()
score_player_2 = Score()
ball = Ball()
game_start()

#Screen listen button press, then move paddle.
screen.listen()
screen.onkey(fun=player_1.up, key='Up')
screen.onkey(fun=player_1.down, key='Down')
screen.onkey(fun=player_2.up, key='w')
screen.onkey(fun=player_2.down, key='s')

game_is_on = True
while game_is_on:

    screen.update() #Update graphical of game.
    time.sleep(0.03) #Represent speed of ball.
    ball.move()

    #Detect collision with wall and paddle while ball move:
    direction_ball = int(ball.heading())
    detect_collision_wall(direction_ball)
    detect_collision_player_1(direction_ball)
    detect_collision_player_2(direction_ball)

    #If player miss the ball, then play again. And plus score for winner.
    if game_over() == True:
        game_start()
        screen.update()
        time.sleep(1)
        # game_is_on = False

