#!/usr/bin/python3
"""Module 0-add_integer.

This module defines add_integer, which adds two
integers or floats together.
"""


def add_integer(a, b=98):
    """Adds a and b.

    Casts float args to int first."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
