from turtle import Turtle

SNAKE_HEAD_POSITION = (0, 0)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = [Turtle(shape='square')]
        self.alive = True

        self.segments[0].penup()
        self.segments[0].goto(x=0, y=0)
        self.segments[0].color('gray')

        self.add_segment()
        self.add_segment()

    def add_segment(self):
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        new_segment.color('white')
        self.segments.append(new_segment)

    def move_forward(self):
        for index, segment in reversed(list(enumerate(self.segments))):
            if index == 0:
                continue

            x = self.segments[index-1].xcor()
            y = self.segments[index-1].ycor()
            segment.goto(x, y)

        self.segments[0].forward(20)

    def check_collision(self, screen_dimensions: tuple = (0, 0)):

        # Body collision
        for segment in self.segments[1:]:
            if segment.distance(self.segments[0].xcor(), y=self.segments[0].ycor()) < 15:
                self.alive = False
                break

        # Border collision
        if self.segments[0].xcor() >= screen_dimensions[0] / 2 or self.segments[0].xcor() <= -screen_dimensions[0] / 2:
            self.alive = False

        if self.segments[0].ycor() >= screen_dimensions[1] / 2 or self.segments[0].ycor() <= -screen_dimensions[1] / 2:
            self.alive = False

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
