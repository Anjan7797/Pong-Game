import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from net import Net


TOP_WALL = 285
RIGHT_WALL = 385
PADDLE_COLLISION_DETECTION = 45


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()
score = Scoreboard()
net = Net()

game_is_on = True
game_state = "playing"

screen.listen()


def pause_game():
    """Toggle between playing and manual pause."""

    global game_state

    if game_state == "playing":
        game_state = "pause"
    elif game_state == "pause":
        game_state = "playing"


def quit_game():
    """Exit the main game loop."""

    global game_is_on
    game_is_on = False


# Keyboard controls
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(pause_game, "space")
screen.onkey(quit_game, "q")


# Records when a score pause begins.
pause_start_time = time.time()


while game_is_on:

    # Frame rate is controlled by the ball's current speed.
    time.sleep(ball.move_speed)
    screen.update()

    if game_state == "playing":

        ball.move()

        # Bounce off the top and bottom walls.
        if ball.ycor() > TOP_WALL or ball.ycor() < -TOP_WALL:
            ball.bounce_y()

        # Left player scores.
        if ball.xcor() > RIGHT_WALL:

            score.increase_left_score()
            winner = score.check_winner()

            if winner:
                score.game_over(winner)
                screen.update()
                game_is_on = False
            else:
                pause_start_time = time.time()
                game_state = "score_pause"

        # Right player scores.
        if ball.xcor() < -RIGHT_WALL:

            score.increase_right_score()
            winner = score.check_winner()

            if winner:
                score.game_over(winner)
                screen.update()
                game_is_on = False
            else:
                pause_start_time = time.time()
                game_state = "score_pause"

        # Bounce only when the ball is moving toward a paddle.
        if (
            ball.distance(right_paddle) < PADDLE_COLLISION_DETECTION and ball.x_move > 0
            or
            ball.distance(left_paddle) < PADDLE_COLLISION_DETECTION and ball.x_move < 0
        ):
            ball.bounce_x()
            ball.speed_up()

    # Brief pause after each point before serving again.
    if game_state == "score_pause":

        if time.time() - pause_start_time > 0.1:
            ball.reset_position()
            game_state = "playing"


screen.exitonclick()