from turtle import Screen
from modules.game import *
from modules.snake import *

FOOD_NUMBER = 5
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def window_setup(screen, snake):
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor('black')
    screen.title('Snakezaum')

    screen.tracer(0)
    screen.listen()
    screen.onkey(snake.move_up, 'Up')
    screen.onkey(snake.move_down, 'Down')
    screen.onkey(snake.move_left, 'Left')
    screen.onkey(snake.move_right, 'Right')


def main():
    screen = Screen()
    snake = Snake()

    window_setup(screen, snake)

    game = Game(snake=snake, food_num=FOOD_NUMBER, screen=screen, screen_dimensions=(SCREEN_WIDTH, SCREEN_HEIGHT))
    game.play()

    screen.exitonclick()


if __name__ == '__main__':
    main()

