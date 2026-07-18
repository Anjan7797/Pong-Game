from turtle import Turtle


class Net:
    """Draws the dashed center line of the Pong court."""

    def __init__(self):
        self.create_dash_line()

    @staticmethod
    def create_segment(x, y):
        """Create a single dash segment at the given position."""
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(x, y)
        return segment

    def create_dash_line(self):
        """Build the center dashed line from individual segments."""

        x = 0
        start_y = 300

        for i in range(15):
            # Place each segment 40 pixels apart:
            # 20 px for the dash itself and 20 px for the gap.
            current_y = start_y - (i * 40)
            self.create_segment(x, current_y)