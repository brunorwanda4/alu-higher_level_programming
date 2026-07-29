#!/usr/bin/python3
"""Module 2-append_write"""


def append_write(filename="", text=""):
    """Appends a string to end of a text file (UTF8), returns nb chars added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
