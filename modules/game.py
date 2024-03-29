from modules.food import *
from modules.HUD import *
import time


class Game:
    def __init__(self, snake=None, food_num=None, screen=None, screen_dimensions: tuple = (0, 0)):
        self.snake = snake
        self.screen = screen
        self.screen_dimensions = screen_dimensions
        self.food_num = food_num
        self.score = 0
        self.HUD = HUD(screen_dimensions)

        self.food_list = list()
        for i in range(food_num):
            food = Food(screen_dimensions)
            self.food_list.append(food)

    def remaining_food(self) -> list:
        remaining = list()
        for food in self.food_list:
            if self.snake.segments[0].distance(food.x_cord, y=food.y_cord) > 15:
                remaining.append(food)
            else:
                self.score += 1
                self.snake.add_segment()
                food.plot.reset()

        return remaining

    def update_food_list(self, remaining):
        while len(remaining) < self.food_num:
            food = Food(self.screen_dimensions)
            remaining.append(food)
        self.food_list = remaining

    def play(self):
        self.screen.update()

        while self.snake.alive:
            time.sleep(.1)

            self.snake.move_forward()
            self.snake.check_collision(self.screen_dimensions)
            self.update_food_list(self.remaining_food())
            self.HUD.update_score(self.score)

            self.screen.update()

        self.HUD.game_over()
