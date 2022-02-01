from turtle import Turtle
PLAYER_STARTING_POSITION = (420, 0)
COMPUTER_STARTING_POSITION = (-420, 0)


class Paddle(Turtle):
    def __init__(self, player_type):
        super().__init__()
        self.y_pos = 0
        self.paddle = Turtle("square")
        self.paddle.penup()
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=3, stretch_len=1)

        # Create instance of a turtle based on type of an player
        if player_type == "player":
            self.paddle.goto(PLAYER_STARTING_POSITION)
        elif player_type == "computer":
            self.paddle.goto(COMPUTER_STARTING_POSITION)

    def paddle_pos(self):
        return self.paddle.position()

    def move_up(self):
        if self.paddle.ycor() < 260:
            self.y_pos += 20
            self.paddle.sety(self.y_pos)

    def move_down(self):
        if self.paddle.ycor() > - 260:
            self.y_pos -= 20
            self.paddle.sety(self.y_pos)
