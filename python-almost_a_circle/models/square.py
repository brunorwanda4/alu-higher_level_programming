#!/usr/bin/python3
"""Defines the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of the Square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Retrieves the size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size (assigns width then height)"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates attributes via no-keyword or keyworded arguments"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
