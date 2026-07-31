#!/usr/bin/python3
"""Define a square with its own string representation."""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represent a square with a positive integer size."""

    def __init__(self, size):
        """Initialize a square after validating its size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the square's description."""
        return "[Square] {}/{}".format(self.__size, self.__size)
