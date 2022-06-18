from modules.food import *
import time


class Game:
    def __init__(self, snake=None, food_num=None, screen=None):
        self.snake = snake
        self.screen = screen
        self.food_num = food_num

    def play(self):
        self.screen.update()

        while self.snake.alive:
            time.sleep(.1)

            self.snake.move_forward()
            self.snake.check_collision()

            self.screen.update()

