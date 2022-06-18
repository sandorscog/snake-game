from turtle import Screen
from modules.game import *
from modules.snake import *

FOOD_NUMBER = 1

def window_setup(screen, snake):
    screen.setup(width=600, height=600)
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

    game = Game(snake=snake, food_num=FOOD_NUMBER, screen=screen)

    game.play()

    screen.exitonclick()


if __name__ == '__main__':
    main()

