#!/usr/bin/python3
"""Module 5-text_indentation"""


def text_indentation(text):
    """Prints text with 2 new lines after each ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    buf = ""
    for char in text:
        buf += char
        if char in ".?:":
            print(buf.strip())
            print()
            buf = ""
    print(buf.strip(), end="")
