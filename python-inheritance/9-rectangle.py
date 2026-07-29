#!/usr/bin/python3
"""Module 9-rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a new Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
