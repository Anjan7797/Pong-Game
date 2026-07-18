from turtle import Turtle


class Ball(Turtle):
    """Represents the game ball and controls its movement."""

    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        """
        Move the ball one frame using its current movement values.
        Position updates are handled only by this method.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Reverse the vertical movement direction.

        This method only changes the ball's future movement.
        The actual position update is performed by move().
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Reverse the horizontal movement direction.

        This method only changes the ball's future movement.
        Position updates remain the responsibility of move().
        """
        self.x_move *= -1

    def reset_position(self):
        """
        Return the ball to the center and send it toward
        the player who just conceded the point.
        """
        self.goto(0, 0)
        self.x_move *= -1

    def speed_up(self):
        """
        Increase the ball's speed by reducing the delay
        between consecutive frames.
        """
        self.move_speed -= (self.move_speed * 10) / 100