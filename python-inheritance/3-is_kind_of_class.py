#!/usr/bin/python3
"""Provide a class and subclass membership check."""


def is_kind_of_class(obj, a_class):
    """Return whether ``obj`` is an instance of ``a_class`` or a subclass."""
    return isinstance(obj, a_class)
