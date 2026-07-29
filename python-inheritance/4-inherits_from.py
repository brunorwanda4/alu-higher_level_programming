#!/usr/bin/python3
"""Module 4-inherits_from"""


def inherits_from(obj, a_class):
    """Returns True if obj is instance of a class that inherited
    (directly or indirectly) from a_class"""
    return isinstance(obj, a_class) and type(obj) != a_class
