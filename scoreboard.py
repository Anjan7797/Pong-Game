from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 40, "bold")
GAME_OVER_FONT = ("Arial", 30, "bold")


class Scoreboard:

    def __init__(self):
        # Current score for each player.
        self.left_score = 0
        self.right_score = 0

        # Turtle used to display the left player's score.
        self.left_pen = Turtle()
        self.left_pen.hideturtle()
        self.left_pen.color("white")
        self.left_pen.penup()
        self.left_pen.goto(-100, 240)
        self.update_score(self.left_pen, self.left_score)

        # Turtle used to display the right player's score.
        self.right_pen = Turtle()
        self.right_pen.hideturtle()
        self.right_pen.color("white")
        self.right_pen.penup()
        self.right_pen.goto(100, 240)
        self.update_score(self.right_pen, self.right_score)

        # Separate Turtle used for the game over message.
        self.game_over_pen = Turtle()
        self.game_over_pen.hideturtle()
        self.game_over_pen.penup()
        self.game_over_pen.color("red")
        self.game_over_pen.goto(0, 0)

    def update_score(self, pen, score):
        """
        Refresh the score displayed by the given Turtle.

        Args:
            pen: Turtle responsible for drawing the score.
            score: Current score to display.
        """
        pen.clear()
        pen.write(f"{score}", align=ALIGNMENT, font=FONT)

    def increase_right_score(self):
        """Increase the right player's score and refresh the display."""
        self.right_score += 1
        self.update_score(self.right_pen, self.right_score)

    def increase_left_score(self):
        """Increase the left player's score and refresh the display."""
        self.left_score += 1
        self.update_score(self.left_pen, self.left_score)

    def check_winner(self):
        """
        Check whether either player has reached the winning score.

        Returns:
            "Right" if the right player wins.
            "Left" if the left player wins.
            None if the game should continue.
        """
        if self.right_score == 10:
            return "Right"
        elif self.left_score == 10:
            return "Left"
        return None

    def game_over(self, winner):
        """
        Display the final game over message.

        The winner is provided by check_winner(); this method is
        responsible only for displaying the result.
        """
        self.game_over_pen.clear()
        self.game_over_pen.write(
            f"GAME OVER\n{winner} PLAYER WINS",
            align=ALIGNMENT,
            font=GAME_OVER_FONT
        )