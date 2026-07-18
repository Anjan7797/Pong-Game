from turtle import Turtle

MOVE_DISTANCE = 20
TOP_LIMIT = 250
BOTTOM_LIMIT = -250


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        # Stretching the height by 5 creates a 100 px paddle.
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        """Predict the next position before moving.
           The paddle moves only if its center remains within the screen bounds.
           """
        new_y = self.ycor() + MOVE_DISTANCE

        if new_y <= TOP_LIMIT:
            self.goto(self.xcor(), new_y)

    def down(self):
        """Predict the next position before moving.
           This prevents any part of the paddle from leaving the screen.
           """
        new_y = self.ycor() - MOVE_DISTANCE

        if new_y >= BOTTOM_LIMIT:
            self.goto(self.xcor(), new_y)