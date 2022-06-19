from turtle import Turtle
import random


class Food:
    def __init__(self, screen_dimension: tuple = (0, 0)):
        self.plot = Turtle('circle')
        self.plot.penup()
        self.plot.color('red')
        self.plot.shapesize(stretch_wid=.5, stretch_len=.5)

        canvas_bound = (int((screen_dimension[0] - 50) / 2), int((screen_dimension[1] - 50) / 2))
        self.x_cord = random.randint(-canvas_bound[0], canvas_bound[0])
        self.y_cord = random.randint(-canvas_bound[1], canvas_bound[1])
        self.plot.goto(self.x_cord, self.y_cord)
