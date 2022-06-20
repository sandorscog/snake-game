from turtle import Turtle


class HUD(Turtle):
    def __init__(self, screen_dimensions: tuple = (0, 0)):
        super().__init__()
        self.score = 0
        self.color('red')
        self.penup()
        self.goto(x=0, y=screen_dimensions[1]/2 - 20)
        self.hideturtle()
        self.write(f'Score: {self.score}', align='center', font=('Arial', 10, 'normal'))

    def update_score(self, score):
        self.clear()
        self.write(f'Score: {score}', align='center', font=('Arial', 10, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER',  align='center', font=('Arial', 25, 'normal'))
