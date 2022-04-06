from turtle import Turtle
from random import randint, choice
FOOD_COLOR = ["seashell", "cyan", "pale green", "snow", "gold", "green yellow", "bisque", "hot pink", "deep pink",
              "crimson"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh_food_pos()

    def refresh_food_pos(self):
        self.color(choice(FOOD_COLOR))
        random_x_pos = randint(-270, 270)
        random_y_pos = randint(-270, 270)
        self.goto(random_x_pos, random_y_pos)
