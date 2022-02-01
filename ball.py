import random
import time
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball = Turtle("square")
        self.ball.color("blue")
        self.ball.penup()
        self.y_pos = self.ball.ycor()
        self.x_pos = self.ball.xcor()

        self.x_direction = random.choice([-1, 1])
        self.y_direction = random.choice([-1, 1])

        self.refresh()

    def refresh(self):
        self.y_pos = random.randint(-200, 200)
        self.x_pos = 0
        self.x_direction = random.choice([-1, 1])
        self.y_direction = random.choice([-1, 1])
        self.ball.goto(0, self.y_pos)

    def move(self):
        time.sleep(0.000000000000000000000001)
        self.x_pos += 3 * self.x_direction
        self.y_pos += 3 * self.y_direction
        self.ball.goto(self.x_pos, self.y_pos)

    def bounce(self):
        if self.x_direction == 1 and self.y_direction == 1:
            self.x_direction = 1
            self.y_direction = -1

        elif self.x_direction == 1 and self.y_direction == -1:
            self.x_direction = 1
            self.y_direction = 1

        elif self.x_direction == -1 and self.y_direction == 1:
            self.x_direction = -1
            self.y_direction = -1

        elif self.x_direction == - 1 and self.y_direction == -1:
            self.x_direction = -1
            self.y_direction = 1

    def paddle_bounce(self):
        if self.x_direction == -1 and self.y_direction == 1:
            self.x_direction = 1
            self.y_direction = 1

        elif self.x_direction == - 1 and self.y_direction == -1:
            self.x_direction = 1
            self.y_direction = -1

        elif self.x_direction == 1 and self.y_direction == 1:
            self.x_direction = -1
            self.y_direction = 1

        elif self.x_direction == 1 and self.y_direction == -1:
            self.x_direction = -1
            self.y_direction = -1
