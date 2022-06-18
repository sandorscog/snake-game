from turtle import Turtle

SNAKE_HEAD_POSITION = (0, 0)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = [Turtle(shape='square'), Turtle(shape='square'), Turtle(shape='square')]
        self.alive = True

        for index, segment in enumerate(self.segments):
            segment.penup()
            segment.goto(x=SNAKE_HEAD_POSITION[0] - (index * 20), y=SNAKE_HEAD_POSITION[1])
            segment.color('white')

    def move_forward(self):
        for index, segment in reversed(list(enumerate(self.segments))):
            if index == 0:
                continue

            x = self.segments[index-1].xcor()
            y = self.segments[index-1].ycor()
            segment.goto(x, y)

        self.segments[0].forward(20)

    def check_collision(self):
        for index, segment in enumerate(self.segments):
            if index == 0:
                continue

            if segment.xcor() == self.segments[0].xcor() and segment.ycor() == self.segments[0].ycor():
                self.alive = False
                break

    def add_segment(self):
        pass

    def move_up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def move_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def move_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def move_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
