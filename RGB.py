from random import random as rn


class RGB:
    """
    The RGB® Color Module.
    Represents an RGB® color object with features for handling hexadecimal and RGB types.
    To avoid Errors and Confusion, the object only accepts numbers between 0 and 1 to initialization.
    # Features: Allows creation of new colors based on an existing one (seed)

    author: MKinG©™
    time: 1715816023.4784908"
    """

    def __init__(self, r=None, g=None, b=None):
        """
        Initialize RGB® color object.
        Generate or assign colors 'Red', 'Green' and 'Blue'.
        - convert the provided argument(s) to float value(s), a number between 0 and 1
        - 'None' value argument(s) will be assigned randomize

        :param r: Red color value (0 to 1), defaults to None.
        :param g: Green color value (0 to 1), defaults to None.
        :param b: Blue color value (0 to 1), defaults to None.
        """

        # Generate or assign color values
        self.r = self.generator(r)
        self.g = self.generator(g)
        self.b = self.generator(b)

    def __repr__(self):
        """
        Representation of RGB color object.
        Validates 'self.r', 'self.g', and 'self.b' each time the object is called.

        :return: String representation of the RGB color object.
        """

        self.check_values()  # Validate color values
        return f"RGB® color Object ⧉ {self.version} Value: {self.rgb} | ID:{id(self)} "

    def __str__(self):
        """String representation of RGB® color as Hexadecimal type."""
        return self.hex  # Ex: #ffffff

    def __iter__(self):
        """Iterator representation of RGB® color."""
        return iter(self.rgb)  # Ex: (0-1, 0-1, 0-1)

    def __len__(self):
        """Length of RGB® color Iterator."""
        return len(self.rgb)

    @staticmethod
    def to_hex(number: float) -> str:
        """
        Convert a number between 0 and 1 to hexadecimal format.
        - tools for 'hex()' function
        # Feature: convert hex-format to rgb

        :param number: Number between 0 and 1.
        :return: Hexadecimal representation of the number.
        """

        return hex(int(number * 255))[2:].zfill(2)

    @staticmethod
    def to_cir(number: float) -> int:
        """
        Convert a number between 0 and 1 to a color value within the circular color space (0 to 255).
        - tools for 'cir()' function
        # Feature: convert cir-format to rgb

        :param number: Number between 0 and 1.
        :return: Number in the range of 0 to 255 as int.
        """

        return int(number * 255)

    @staticmethod
    def generator(number=None) -> float:
        """
        Generate a random or specified color value.
        - 'None' value argument(s) will be assigned randomized
        - ensure the value will be a number between 0 and 1
        # Feature: get range to generate a random number in a specific range

        :param number: A number between 0 and 1, defaults to None.
        :return: Random color value if None, otherwise returns the input value.
        """

        # If number is 'None', generate a random number for color
        if number is None:
            return rn()  # Output: 0.000 ~ 1.000
        # If number can be converted to float()
        elif isinstance(float(number), float):
            if number > 1:
                return float(1)  # If number exceeds 1, return the maximum value of 1
            elif number < 0:
                return float(0)  # If number is less than 0, return the minimum value of 0
            else:
                return float(number)  # Trick: min(max(number, 0.0), 1.0)

    @property
    def rgb(self) -> tuple:
        """
        Return the RGB® color values as 'tuple(r,g,b)'. (Original Method)
        - formated numbers are floats with only 3 number after point (Ex: 0.123456789 -> 0.123)
        - Output: (0-1, 0-1, 0-1)

        :return: Tuple containing (R, G, B) color values.
        """

        # Format color values to 3 decimal places
        r = float("{:.3f}".format(self.r))
        g = float("{:.3f}".format(self.g))
        b = float("{:.3f}".format(self.b))
        return r, g, b

    @property
    def cir(self) -> tuple:
        """
        Get the circular color space representation of the current RGB® color values.
        - Output: (0-255, 0-255, 0-255)

        :return: Tuple containing (R, G, B) color values in the range of 0 to 255.
        """

        # Convert RGB® color values to circular color space (0-255)
        cir_r = self.to_cir(self.r)
        cir_g = self.to_cir(self.g)
        cir_b = self.to_cir(self.b)
        return cir_r, cir_g, cir_b

    @property
    def hex(self) -> str:
        """
        Get the hexadecimal representation of the current RGB® color values.
        - Output: #ffffff

        :return: Hexadecimal representation of the RGB® color.
        """

        # Convert RGB® color values to hexadecimal as string
        hex_r = self.to_hex(self.r)
        hex_g = self.to_hex(self.g)
        hex_b = self.to_hex(self.b)
        return f"#{hex_r}{hex_g}{hex_b}"

    @property
    def version(self) -> str:
        """Get the version of the RGB® color object."""
        return f"v0.4.7 №0"  # No:0

    def check_values(self) -> None:
        """
        Check and validate the RGB® color values.
         - ensure the values of 'self.r', 'self.g' and 'self.b' are between 0 and 1
        """

        # Validate and correct color values
        self.r = self.generator(self.r)
        self.g = self.generator(self.g)
        self.b = self.generator(self.b)

    def random_color(self, r=None, g=None, b=None) -> tuple:
        """
        Generate a random RGB® color.
        - random number for all parameters except the given parameter(s)
        - 'None' value argument(s) will be assigned randomize

        :param r: Red color value (0 to 1), defaults to None.
        :param g: Green color value (0 to 1), defaults to None.
        :param b: Blue color value (0 to 1), defaults to None.
        :return: Tuple containing (R, G, B) color values.
        """

        # Generate or assign color values
        self.r = self.generator(r)
        self.g = self.generator(g)
        self.b = self.generator(b)
        return self.rgb

    def reset_color(self, r=None, g=None, b=None) -> tuple:
        """
        Reset RGB® color values.
        - Reset only the given parameter(s) and don't change the others
        - 'None' value argument(s) won't be changed

        :param r: New red color value (0 to 1), defaults to None.
        :param g: New green color value (0 to 1), defaults to None.
        :param b: New blue color value (0 to 1), defaults to None.
        :return: Tuple containing (R, G, B) color values.
        """

        # Reset specified color values, keep others unchanged
        self.r = self.generator(r) if r is not None else self.r
        self.g = self.generator(g) if g is not None else self.g
        self.b = self.generator(b) if b is not None else self.b
        return self.rgb
