#!/usr/bin/python3
"""Define a base geometry class with integer validation."""


class BaseGeometry:
    """Provide shared behavior for geometry classes."""

    def area(self):
        """Raise an exception because subclasses must implement area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that ``value`` is a strictly positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
