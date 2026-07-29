#!/usr/bin/python3
"""Module 7-base_geometry"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Raises an Exception, area() not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
