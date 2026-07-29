#!/usr/bin/python3
"""Provide a strict inheritance check."""


def inherits_from(obj, a_class):
    """Return whether ``obj`` belongs to a strict subclass of ``a_class``."""
    return isinstance(obj, a_class) and type(obj) is not a_class
