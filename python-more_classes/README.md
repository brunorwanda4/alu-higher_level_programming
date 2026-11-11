# Python - More Classes and Objects

This project delves deeper into Object-Oriented Programming (OOP) in Python, covering class and instance attributes, data abstraction and encapsulation, getters and setters, special methods (`__str__`, `__repr__`, `__del__`), static methods (`@staticmethod`), class methods (`@classmethod`), and the N queens backtracking algorithm.

## Files

| File | Description |
| --- | --- |
| `0-rectangle.py` | Empty class `Rectangle` that defines a rectangle. |
| `1-rectangle.py` | Class `Rectangle` with private attributes `width` and `height`, with property getters and setters validating types and values. |
| `2-rectangle.py` | Class `Rectangle` with public instance methods `area()` and `perimeter()`. |
| `3-rectangle.py` | Class `Rectangle` with `__str__` returning printable `#` characters. |
| `4-rectangle.py` | Class `Rectangle` with `__repr__` returning a representation to recreate the instance via `eval()`. |
| `5-rectangle.py` | Class `Rectangle` with `__del__` printing `Bye rectangle...` upon instance deletion. |
| `6-rectangle.py` | Class `Rectangle` tracking the number of active instances with `number_of_instances`. |
| `7-rectangle.py` | Class `Rectangle` with customizable `print_symbol` class attribute. |
| `8-rectangle.py` | Class `Rectangle` with static method `bigger_or_equal(rect_1, rect_2)` comparing rectangles by area. |
| `9-rectangle.py` | Class `Rectangle` with class method `square(cls, size=0)` returning a square Rectangle instance. |
| `10-class-and-instance-attributes.md` | Comprehensive technical blog post covering Python class vs. instance attributes and `__dict__`. |
| `101-nqueens.py` | Python script solving the N queens puzzle using backtracking. |
