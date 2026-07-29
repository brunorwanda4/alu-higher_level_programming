#!/usr/bin/python3
"""Provide a function for inspecting an object's attributes."""


def lookup(obj):
    """Return the available attributes and methods of ``obj``."""
    return dir(obj)
