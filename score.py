from turtle import Turtle

ALLIGMENT = "center"
FONT = ("Futura", 18, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.computer_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")

        self.display_player_score()
        self.display_computer_score()

    def increase_score(self, player_miss, computer_miss):

        if player_miss is True:
            self.clear()
            self.computer_score += 1
            self.display_computer_score()
            self.display_player_score()
        elif computer_miss is True:
            self.clear()
            self.player_score += 1
            self.display_computer_score()
            self.display_player_score()

    def display_player_score(self):
        self.goto(-140, 270)
        self.write(f"MARCIA: {self.player_score}", True, align=ALLIGMENT, font=FONT)

    def display_computer_score(self):
        self.goto(140, 270)
        self.write(f"MICHAŁ: {self.computer_score}", True, align=ALLIGMENT, font=FONT)