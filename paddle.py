from turtle import Turtle

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 600
STARTING_POSITION = [(0, -20), (0, 0), (0, 20)]
MOVE_DISTANCE = 20
PLAYER_1_POSITION = int(-SCREEN_WIDTH / 2) + 20
PLAYER_2_POSITION = int(SCREEN_WIDTH / 2) - 20
SPEED = 'fastest'
UP = 90
DOWN = 270

class Paddle():

	def __init__(self):
		self.segments = []
		self.create_paddle()


	def create_paddle(self):
		'''
		Create a segment of paddle. Return a segment.
		'''
		for position in STARTING_POSITION:
			new_segment = Turtle('square')
			new_segment.color('white')
			new_segment.penup()
			new_segment.speed(SPEED)
			new_segment.goto(position)
			self.segments.append(new_segment)


	def move(self, direction):
		'''
		Move paddle.
		'''
		for seg_num in self.segments:
			seg_num.setheading(direction)
			seg_num.forward(MOVE_DISTANCE)


	def player_1_start(self):
		'''
		Generate starting position for player 1.
		'''
		for seg_num in self.segments:
			seg_num.setx(PLAYER_1_POSITION)


	def player_2_start(self):
		'''
		Generate starting position for player 2.
		'''
		for seg_num in self.segments:
			seg_num.setx(PLAYER_2_POSITION)


	def up(self):
		'''
		Paddle move up.
		'''
		self.move(UP)


	def down(self):
		'''
		Paddle move down.
		'''
		self.move(DOWN)
