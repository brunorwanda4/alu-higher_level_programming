#!/usr/bin/python3
"""Define a base geometry class with an abstract area operation."""


class BaseGeometry:
    """Represent a geometry whose area is not yet implemented."""

    def area(self):
        """Raise an exception because subclasses must implement area."""
        raise Exception("area() is not implemented")
