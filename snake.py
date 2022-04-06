from turtle import Turtle
from random import choice
SNAKE_STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SNAKE_COLOR = ["seashell", "cyan", "pale green", "snow", "gold", "green yellow", "bisque", "hot pink", "deep pink",
               "crimson"]


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def create_snake(self):
        for pos in SNAKE_STARTING_POS:
            self.add_snake(pos)

    def add_snake(self, pos):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color(choice(SNAKE_COLOR))
        snake.goto(pos)
        self.snake_segments.append(snake)

    def extend(self):
        self.add_snake(self.snake_segments[-1].position())

    def move(self):
        for pos in range(len(self.snake_segments) - 1, 0, -1):
            new_xcor = self.snake_segments[pos - 1].xcor()
            new_ycor = self.snake_segments[pos - 1].ycor()
            self.snake_segments[pos].goto(new_xcor, new_ycor)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
