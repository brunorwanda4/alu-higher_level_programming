#!/usr/bin/python3
"""Define a complete rectangle implementation."""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle with positive integer dimensions."""

    def __init__(self, width, height):
        """Initialize a rectangle after validating its dimensions."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the rectangle's area."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle's description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
