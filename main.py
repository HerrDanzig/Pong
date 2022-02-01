# TODO: Create the screen ✔
# TODO: Create and move a paddle ✔
# TODO: Create another paddle ✔
# TODO: Create the ball and make it move ✔
# TODO: Detect collision with wall and bounce ✔
# TODO: Detect collision with paddle ✔
# TODO: Detect when paddle misses ✔
# TODO: Keep score ✔
import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("PONG THE GAME")
screen.tracer(0)

# Display net over screen
net = Turtle("square")
net.color("white")
net.shapesize(stretch_wid=28, stretch_len=0.25)

player = Paddle("player")
computer = Paddle("computer")
ball = Ball()
score = Score()

# Move the paddle
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")
screen.onkeypress(computer.move_up, "w")
screen.onkeypress(computer.move_down, "s")

game_is_on = True
wall_collision = False
paddle_collision = False

while game_is_on is True:
    screen.update()
    # Detect when paddle misses the ball
    if ball.x_pos < -440:
        score.increase_score(True, False)
        wall_collision = False
        paddle_collision = False
        ball.refresh()
        screen.update()
        time.sleep(1)

    elif ball.x_pos > 440:
        score.increase_score(False, True)
        wall_collision = False
        paddle_collision = False
        ball.refresh()
        screen.update()
        time.sleep(1)

    # Detect collision with paddle
    if (ball.ball.distance(player.paddle) < 20 or ball.ball.distance(computer.paddle) < 20) \
            and paddle_collision is False:
        ball.paddle_bounce()

    # Detect ball collision with wall
    if ball.y_pos > 280 or ball.y_pos < -280:
        ball.bounce()
    ball.move()

    screen.listen()
screen.exitonclick()
