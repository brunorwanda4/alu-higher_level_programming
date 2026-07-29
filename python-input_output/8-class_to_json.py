#!/usr/bin/python3
"""Module 8-class_to_json"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of obj"""
    return obj.__dict__
