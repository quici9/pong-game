from turtle import Turtle
import random

MOVE_DISTANCE = 10
DIRECTION = [45, 135, 225, 315]
SPEED = 'slowest'

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed(SPEED)
        self.shapesize(0.5, 0.5, 0.5)


    def start_game(self):
        self.goto(0, 0)
        start_direction = random.choice(DIRECTION)
        self.setheading(start_direction)


    def move(self):
        self.forward(MOVE_DISTANCE)
