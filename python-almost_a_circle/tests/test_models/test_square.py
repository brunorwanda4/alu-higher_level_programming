#!/usr/bin/python3
"""Unittests for models.square.Square"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Tests instantiation of the Square class"""

    def test_is_rectangle_instance(self):
        self.assertIsInstance(Square(5), Rectangle)

    def test_is_base_instance(self):
        self.assertIsInstance(Square(5), Base)

    def test_width_equals_height(self):
        s = Square(5)
        self.assertEqual(s.width, s.height)
        self.assertEqual(s.width, 5)

    def test_default_x_y(self):
        s = Square(5)
        self.assertEqual((s.x, s.y), (0, 0))

    def test_x_given(self):
        s = Square(2, 2)
        self.assertEqual(s.x, 2)

    def test_x_y_given(self):
        s = Square(3, 1, 3)
        self.assertEqual((s.x, s.y), (1, 3))

    def test_id_given(self):
        s = Square(5, 0, 0, 12)
        self.assertEqual(s.id, 12)

    def test_id_auto(self):
        s1 = Square(5)
        s2 = Square(5)
        self.assertEqual(s2.id, s1.id + 1)

    def test_no_new_attributes(self):
        s = Square(5)
        self.assertNotIn("size", s.__dict__)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Square(5, 0, 0, 1, 2)

    def test_size_validation_inherited_type(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")

    def test_size_validation_inherited_value(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)

    def test_x_validation_inherited(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1)

    def test_y_validation_inherited(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 0, -1)


class TestSquare_str(unittest.TestCase):
    """Tests __str__"""

    def test_str_default(self):
        s = Square(5, id=1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_str_with_x(self):
        s = Square(2, 2, id=2)
        self.assertEqual(str(s), "[Square] (2) 2/0 - 2")

    def test_str_with_x_y(self):
        s = Square(3, 1, 3, id=3)
        self.assertEqual(str(s), "[Square] (3) 1/3 - 3")


class TestSquare_area(unittest.TestCase):
    """Tests the inherited area method"""

    def test_area(self):
        self.assertEqual(Square(5).area(), 25)

    def test_area_after_size_change(self):
        s = Square(5)
        s.size = 3
        self.assertEqual(s.area(), 9)


class TestSquare_display(unittest.TestCase):
    """Tests the inherited display method"""

    def capture(self, sq):
        captured = io.StringIO()
        sys.stdout = captured
        sq.display()
        sys.stdout = sys.__stdout__
        return captured.getvalue()

    def test_display_basic(self):
        output = self.capture(Square(5))
        self.assertEqual(output, "#####\n" * 5)

    def test_display_with_x_y(self):
        output = self.capture(Square(3, 1, 3))
        self.assertEqual(output, "\n\n\n ###\n ###\n ###\n")


class TestSquare_size(unittest.TestCase):
    """Tests the size property"""

    def test_size_getter(self):
        self.assertEqual(Square(5).size, 5)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height, s.size), (10, 10, 10))

    def test_size_setter_type_error(self):
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_size_setter_value_error(self):
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -1


class TestSquare_update_args(unittest.TestCase):
    """Tests update() with *args"""

    def test_update_id(self):
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)

    def test_update_id_size(self):
        s = Square(5)
        s.update(1, 2)
        self.assertEqual((s.id, s.size), (1, 2))

    def test_update_id_size_x(self):
        s = Square(5)
        s.update(1, 2, 3)
        self.assertEqual((s.id, s.size, s.x), (1, 2, 3))

    def test_update_all_args(self):
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")


class TestSquare_update_kwargs(unittest.TestCase):
    """Tests update() with **kwargs"""

    def test_update_x_kwarg(self):
        s = Square(5)
        s.update(x=12)
        self.assertEqual(s.x, 12)

    def test_update_size_y_kwargs(self):
        s = Square(5)
        s.update(size=7, y=1)
        self.assertEqual((s.size, s.y), (7, 1))

    def test_update_id_kwarg(self):
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(s.id, 89)

    def test_kwargs_ignored_if_args_present(self):
        s = Square(5)
        s.update(1, x=100)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.x, 0)


class TestSquare_to_dictionary(unittest.TestCase):
    """Tests to_dictionary()"""

    def test_keys(self):
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        self.assertEqual(set(d.keys()), {"id", "size", "x", "y"})

    def test_values(self):
        s = Square(10, 2, 1, id=1)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_returns_dict_type(self):
        self.assertIsInstance(Square(1).to_dictionary(), dict)

    def test_update_from_dictionary(self):
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))


if __name__ == "__main__":
    unittest.main()
