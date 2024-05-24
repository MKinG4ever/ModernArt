from turtle import Turtle
from RGB import RGB
import random
import math


class ModernArt(Turtle):
    """
    The ModernArt® Module.
    A class to create modern arts using the turtle graphics library.
    Require the RGB® and CustomScreen® modules to initialization.

    author: MKinG©™
    time: 1715070582.8347054"
    """

    def __init__(self, width=1280, height=720):
        """
        Initialize ModernArt® object.
        # Feature: add line style like: dotted, dashed,...

        :param width: Width of drawing board in px.
        :param height: Height of drawing board in px.
        """

        # initialize and create a turtle.Turtle() object
        super().__init__()

        # Width & Height of drawing board
        self.width = width
        self.height = height

        # Turtle attributes
        self.turtle_attr = {
            'speed': 1,
            'color': RGB().hex,
            'shape': 'turtle',
            'shapesize': 2,
            'visible': True
        }

        # Pen attributes
        self.pen_attr = {
            'pensize': 2,
            'pencolor': RGB().hex,
            'visible': True
        }

        # Fill attributes
        self.fill_attr = {
            'fillcolor': RGB().hex,
        }

    def __repr__(self):
        """Representation of ModernArt® object."""
        return f"ModernArt® Object ⧉ {self.version} | ID:{id(self)}"

    @property
    def version(self) -> str:
        """Return the version of the ModernArt® object."""
        return f"v0.7.1 №0"

    @staticmethod
    def random_direction(*args) -> list:
        """
        Return a random direction value between -1 and +1.
        Arguments are multiply by random direction values.
        - for creating point(s) inside the screen

        :param args: Optional arguments to scale the random values.
        :return: A list of scaled random values if args are provided, else a single random value.
        """

        # if: There is an input argument(s)
        if args:
            return [arg * random.random() * random.choice([1, -1]) for arg in args]
        # if: There is no input argument
        else:
            return random.random() * random.choice([1, -1])

    # Turtle Setup
    def setup_turtle(self, speed=None, color=None, shape=None, shapesize=None, visible=None) -> None:
        """
        Set up the turtle with specified attributes.

        :param speed: Speed of the turtle.
        :param color: Color of the turtle.
        :param shape: Shape of the turtle.
        :param shapesize: Size of the turtle shape.
        :param visible: Visibility of the turtle.
        """

        # Shortcut
        attributes = self.turtle_attr

        # Override default attributes if provided
        if speed is not None:
            attributes['speed'] = speed
        if color is not None:
            attributes['color'] = color
        if shape is not None:
            attributes['shape'] = shape
        if shapesize is not None:
            attributes['shapesize'] = shapesize
        if visible is not None:
            attributes['visible'] = visible

        # Set up the turtle with updated attributes
        self.speed(attributes['speed'])
        self.color(attributes['color'])
        self.shape(attributes['shape'])
        self.shapesize(attributes['shapesize'])
        self.hideturtle() if not attributes['visible'] else self.showturtle()

    # Pen Setup
    def setup_pen(self, pensize=None, pencolor=None, visible=None) -> None:
        """
        Set up the pen with specified attributes.

        :param pensize: Size of the pen.
        :param pencolor: Color of the pen.
        :param visible: Visibility of the pen.
        """

        # Shortcut
        attributes = self.pen_attr

        # Update attributes if provided
        if pensize is not None:
            attributes['pensize'] = pensize
        if pencolor is not None:
            attributes['pencolor'] = pencolor
        if visible is not None:
            attributes['visible'] = visible

        # Set up the pen with updated attributes
        self.pensize(attributes['pensize'])
        self.pencolor(attributes['pencolor'])
        self.penup() if not attributes['visible'] else self.pendown()

    # Fill Setup
    def setup_fill(self, fillcolor=None) -> None:
        """
        Set up the fill with specified attributes.

        :param fillcolor: Color of the fill.
        """

        # Shortcut
        attributes = self.fill_attr

        # Update attributes if provided
        if fillcolor is not None:
            attributes['fillcolor'] = fillcolor

        # Set up the fill with updated attributes
        self.fillcolor(attributes['fillcolor'])

    # Full Setup Wizard
    def setup_wizard(self) -> None:
        """
        Fast setup wizard.
        Set up the Turtle, Pen  and Fill with pre-defined attributes.
        # Feature: Sync the colors
        # Feature: Get **kwargs
        """

        self.setup_turtle()  # The turtle
        self.setup_pen()  # The Pen
        self.setup_fill()  # The fill

    # Random color for turtle
    def random_turtle_color(self) -> None:
        """
        Set the turtle color to a random color.
        This will change the 'pencolor()' and 'fillcolor()'.
        - the change won't save as 'turtle.attr'
        # Feature: Change color optional or random
        """

        # Turtle().turtle.color()
        self.color(RGB().hex)

    # Draw a circle mathematical calculation
    def draw_circle_math(self, radius, center_x=None, center_y=None) -> None:
        """
        Draw a circle using mathematical calculations.
        # Feature: show with sin and cos positions as an anim

        :param radius: Radius of the circle.
        :param center_x: x-coordinate of the center.
        :param center_y: y-coordinate of the center.
        """

        # Store the current position of the turtle
        current_x, current_y = self.pos()

        # Determine the center coordinates of the circle
        if center_x is None and center_y is None:
            start_x, start_y = (current_x, current_y)
        else:
            start_x, start_y = (center_x, center_y)

        # Move to start Point | Cover The First Step Glitch
        self.teleport(start_x + radius, start_y)

        # Materials to present position of Sin(y) and Cos(x)
        x_cos = ModernArt()
        y_sin = ModernArt()
        # setup materials
        x_cos.setup_turtle(color=RGB(r=1, g=0, b=0), shape='circle', shapesize=1)
        y_sin.setup_turtle(color=RGB(r=0, g=0, b=1), shape='circle', shapesize=1)
        # Move materials to start position
        x_cos.teleport(start_x, start_y)
        y_sin.teleport(start_x, start_y)

        # Draw the circle using small line segments
        num_segments = 120  # Number of line segments to approximate the circle
        angle_increment = 360 / num_segments

        for _ in range(num_segments):
            # Calculate X and Y
            _x = start_x + (radius * math.cos(math.radians(angle_increment)))
            _y = start_y + (radius * math.sin(math.radians(angle_increment)))

            # Presentation of drawing a Circle through Mathematical calculation
            x_cos.goto(_x, start_y)
            y_sin.goto(start_x, _y)

            # Draw the circle
            self.goto(_x, _y)

            # Turn
            angle_increment += 360 / num_segments

        # Move back in start point
        self.teleport(start_x, start_y)

        # Hide and delete materials
        x_cos.dot(25)
        y_sin.dot(25)
        x_cos.hideturtle()
        y_sin.hideturtle()
        del x_cos
        del y_sin

    # Draw a circle
    def draw_circle(self, radius, center_x=None, center_y=None, fill=False, center_base=True) -> None:
        """
        Draw a circle using built-in circle() function.
        - custom function to make drawings more easily
        - careful about heading, only on 0deg works as expected. may fix with 'rt()' and 'fd()' or use 'setheading()'

        :param radius: Radius of the circle.
        :param center_x: x-coordinate of the center (optional).
        :param center_y: y-coordinate of the center (optional).
        :param fill: Fill the circle or not.
        :param center_base: If true, draw the circle with the current position as the center.
        """

        # Store the current position of the turtle
        current_x, current_y = self.pos()

        # Determine the center coordinates of the circle
        if center_x is None and center_y is None:
            start_x, start_y = (current_x, current_y)
        else:
            start_x, start_y = (center_x, center_y)

        # Move the turtle to the specified center position if center_base is False
        self.teleport(start_x, start_y - radius) if center_base else self.teleport(start_x, start_y)

        # Start filling the shape if fill is True
        if fill:
            self.begin_fill() if fill else None

        # Draw the circle with the specified radius
        self.circle(radius)

        # End filling the shape if fill is True
        if fill:
            self.end_fill()

        # Move the turtle back to the original position
        self.teleport(start_x, start_y)

    # Draw side(s) of a polygon
    def draw_side(self, length, angle, repeat) -> None:
        """
        Draw a side(s) of polygon shape.

        :param length: Length of the side.
        :param angle: Angle to turn after each side.
        :param repeat: Number of sides to draw.
        """

        # Draw side(s)
        for _ in range(repeat):
            self.fd(length)  # Move forward
            self.right(angle)  # Turn right based on the angle

    # Draw a polygon shapes
    def draw_side_shape(self, side_length, sides) -> None:
        """
        Draw a polygon shape.
        Powered by 'draw_side()'.

        :param sides: Number of the polygon sides.
        :param side_length: Length of each side.
        """

        ang = 360 / sides  # Calculate the 'angle' of each turn base on 'sides'
        self.draw_side(side_length, ang, sides)  # Draw

    # Draw a triangle
    def draw_triangle(self, width, angle=120) -> None:
        """
        Draw a Triangle shape.
        Powered by 'draw_side()'.
        - use '-120 degrees' for angle to change the direction of  drawing the triangle.

        :param width: Width of the triangle.
        :param angle: Angle of each corner (default is 120 degrees for an equilateral triangle).
        """

        # Draw a triangle
        self.draw_side(width, angle, 3)

    # Draw a square
    def draw_square(self, width, angle=90) -> None:
        """
        Draw a Square shape.
        Powered by 'draw_side()'.
        - use '-90 degrees' for angle to change the direction of  drawing the triangle.

        :param width: Width of the square.
        :param angle: Angle of each corner (default is 90 degrees for a square).
        """

        # Draw a square
        self.draw_side(width, angle, 4)

    # Draw shapes base on radius with 'circle()'
    def draw_shape(self, radius, sides) -> None:
        """
        Draw shapes with the 'circle()' that based on radius.
        A shadow of 'draw_side_shape()'.

        :param radius: The radius of the hypothetical circle.
        :param sides: The sides of the polygon shape.
        """

        # feature: do the math to calculate width of each side
        self.circle(radius, 360, sides)  # step as 'sides' to complete 360deg. | each turn angle: 'sides' / 360

    # Draw an art with shapes
    # FEATURE
    def draw_art_shapes(self):
        """
        # Feature: with the help of 'draw_side_shape()' and 'draw_shapes()' methods create a new modern art.
        """
        pass

    # Draw a dash
    def draw_dash(self, width) -> None:
        """
        Draw a dash line segment.
        - custom for 'draw_dash_lines()'

        :param width: Length of the dash.
        """

        self.pendown()
        self.fd(width)
        self.penup()

    # Draw an empty space line
    def draw_space(self, width) -> None:
        """
        Move forward without drawing (a space in dash lines).
        - custom 'for draw_dash_lines()'

        :param width: Length of the space.
        """

        self.penup()
        self.fd(width)

    # Draw Dash-Line(s)
    def draw_dash_lines(self, steps, dash_size, space_size) -> None:
        """
        Draw dashed lines.

        :param steps: Number of dashes to draw.
        :param dash_size: Size of each dash.
        :param space_size: Size of each space between dashes.
        """

        for i in range(steps):
            self.draw_space(space_size) if i != 0 else None  # Draw space at the first of each step, Except the first
            self.draw_dash(dash_size)  # Draw dash

    # Random walk drawing
    def draw_random_walk(self, length, steps) -> None:
        """
        Draw a random walk.
        # Feature: walk by reference or relative to the current position
        # Feature: use 'setheading()' or 'left()' or 'right()' to turn
        # Feature: select random or optional color for pen

        :param length: Length of each step.
        :param steps: Number of steps to take.
        """

        for _ in range(steps):
            self.pencolor(*RGB())  # Random pencolor

            # Calculate turn angle
            ang = random.choice([0, 90, 180, 270, 360])
            sig = random.choice([-1, +1])

            # Set up  the angle and draw
            self.setheading(ang * sig)  # you can use '.right()' or '.left()' functions too
            self.forward(length)

    # Draw circles with one share point
    def draw_spiral_circles(self, radius, circles, random_color=False) -> None:
        """
        Draw circles with a shared center point.
        # Feature: get angle for each step

        :param radius: Radius of each circle.
        :param circles: Number of circles to draw.
        :param random_color: Whether to use random colors for each circle.
        """

        ang = 360 // circles  # The angle of each turn
        for heading in range(0, 360, ang):
            self.random_turtle_color() if random_color else None  # Random color
            self.setheading(heading)  # Set angle
            self.circle(radius)  # Draw

    # Draw donat with circles
    def draw_spiral_donat(self, radius, circles, random_color=False) -> None:
        """
        Draw a spiral pattern of circles, resembling a donut shape.

        Each circle is drawn at an angle incremented by a constant value,
        creating a spiral effect. Optionally, random colors can be applied to each circle.

        :param radius: Radius of each circle in the spiral.
        :param circles: Number of circles to draw in the spiral.
        :param random_color: If True, each circle will have a random color (default is False).
        """

        ang = 360 // circles  # The angle of each turn
        for heading in range(0, 360, ang):
            self.random_turtle_color() if random_color else None  # Random color
            self.setheading(heading)  # Set angle

            # Position "B": Drawing part | Create free space in center
            self.penup()
            self.fd(radius)
            self.pendown()

            # Draw
            self.circle(radius)
            # self.circle((radius * (360 - heading) / 360) + (radius * 0.25))

            # Position "A" : The center
            self.penup()
            self.back(radius)

    # Draw dot grid
    def draw_grid_dot(self, width=None, height=None, dot_size=3, times=3) -> None:
        """
        Draw a doted grid.
        # Feature: grid types -> ('Lines', 'Dots')
        # Feature: get x-axis and y-axis times to divide
        # Feature: get start coordinates

        :param width: Width of the grid.
        :param height: Height of the grid.
        :param dot_size: Size of the dot grid.
        :param times: Number of divisions in each direction.
        """

        # Check width and height
        width = self.width if width is None else width
        height = self.height if height is None else height

        # Calculate the screen range
        _x = width // 2
        _y = height // 2

        # Calculate the steps
        x_step = width // times
        y_step = height // times

        # Divide the screen to 'times'
        for x in range(_x * -1, _x + dot_size, x_step):
            for y in range(_y * -1, _y + dot_size, y_step):
                self.teleport(x, y)
                self.dot(dot_size)

    # Draw bubbles all over the Screen
    def draw_bubbles(self, bubbles, radius, random_color=False, fill=True) -> None:
        """
        Draw bubbles on screen in random order.
        # Feature : get range as radius to
        # Feature : expand color to fill_color and pen_color

        :param bubbles: Number of bubbles to draw.
        :param radius: Radius of each bubble.
        :param random_color: Whether to use random colors for each bubble.
        :param fill: Whether to fill the bubbles with color.
        """

        # Screen Width and Height
        size = (self.width // 2, self.height // 2)

        for _ in range(bubbles):
            self.color(RGB().hex) if random_color else None  # 'color()' will change 'pencolor()' and 'fillcolor()'
            _x, _y = self.random_direction(*size)  # Random position in screen
            self.draw_circle(radius=radius, center_x=_x, center_y=_y, fill=fill, center_base=True)  # Draw

    # Draw the First ModernArt
    def draw_dot_dots(self, step, radius, random_color=True) -> None:
        """
        The VeryFirst ModernArt®: Dot Dots v1.
        Draw sorted circles on screen with random styles.
        # Feature: draw the art in the center of the screen

        :param step: Distance between each dot.
        :param radius: Radius of each dot.
        :param random_color: Whether to use random colors for each dot.
        """

        # Calculate the screen range
        x_range = self.width // 2
        y_range = self.height // 2

        for _x in range(step + x_range * -1, x_range, step):
            for _y in range(step + y_range * -1, y_range, step):
                _color = RGB().hex if random_color else self.fill_attr['fillcolor']
                self.teleport(_x, _y)
                self.dot(radius, _color)

    # Modules info/help
    def info(self) -> None:
        """
        Information about for The ModernArt®.
        Basic help to use this module.
        """
        print(self.__repr__())
        print(f"Width:{self.width} × Height:{self.height}")
