#!/usr/bin/python3
"""Module 4-print_square"""


def print_square(size):
    """Prints a square of size x size with the # character"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
