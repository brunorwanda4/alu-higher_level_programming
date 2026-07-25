#!/usr/bin/python3
"""Define a list subclass with sorted display support."""


class MyList(list):
    """Represent a list that can print a sorted copy of itself."""

    def print_sorted(self):
        """Print the list's elements in ascending order."""
        print(sorted(self))
