#!/usr/bin/python3
"""Unittests for models.rectangle.Rectangle"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Tests instantiation of the Rectangle class"""

    def test_is_base_instance(self):
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Base)

    def test_width_height(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)

    def test_default_x_y(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_x_y_given(self):
        r = Rectangle(10, 2, 3, 4)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_id_given(self):
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_id_auto(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, r1.id + 1)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, 0, 1, 2)

    def test_missing_args(self):
        with self.assertRaises(TypeError):
            Rectangle(10)


class TestRectangle_width_validation(unittest.TestCase):
    """Tests width validation"""

    def test_width_not_int_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_width_not_int_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.5, 2)

    def test_width_not_int_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_width_setter(self):
        r = Rectangle(10, 2)
        r.width = 20
        self.assertEqual(r.width, 20)

    def test_width_setter_negative(self):
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10


class TestRectangle_height_validation(unittest.TestCase):
    """Tests height validation"""

    def test_height_not_int(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_height_setter(self):
        r = Rectangle(10, 2)
        r.height = 20
        self.assertEqual(r.height, 20)


class TestRectangle_x_validation(unittest.TestCase):
    """Tests x validation"""

    def test_x_not_int(self):
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = {}

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1)

    def test_x_zero_allowed(self):
        r = Rectangle(10, 2, 0)
        self.assertEqual(r.x, 0)

    def test_x_setter(self):
        r = Rectangle(10, 2)
        r.x = 5
        self.assertEqual(r.x, 5)


class TestRectangle_y_validation(unittest.TestCase):
    """Tests y validation"""

    def test_y_not_int(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, "0")

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_y_setter(self):
        r = Rectangle(10, 2)
        r.y = 5
        self.assertEqual(r.y, 5)


class TestRectangle_area(unittest.TestCase):
    """Tests the area method"""

    def test_area_basic(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_area_square_shape(self):
        self.assertEqual(Rectangle(2, 10).area(), 20)

    def test_area_with_offset(self):
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_area_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 2).area(1)


class TestRectangle_display(unittest.TestCase):
    """Tests the display method"""

    def capture(self, rect):
        captured = io.StringIO()
        sys.stdout = captured
        rect.display()
        sys.stdout = sys.__stdout__
        return captured.getvalue()

    def test_display_basic(self):
        output = self.capture(Rectangle(4, 6))
        expected = "####\n" * 6
        self.assertEqual(output, expected)

    def test_display_small(self):
        output = self.capture(Rectangle(2, 2))
        self.assertEqual(output, "##\n##\n")

    def test_display_with_x_y(self):
        output = self.capture(Rectangle(2, 3, 2, 2))
        self.assertEqual(output, "\n\n  ##\n  ##\n  ##\n")

    def test_display_with_x_only(self):
        output = self.capture(Rectangle(3, 2, 1, 0))
        self.assertEqual(output, " ###\n ###\n")


class TestRectangle_str(unittest.TestCase):
    """Tests __str__"""

    def test_str_full(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_default_y(self):
        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), "[Rectangle] ({}) 1/0 - 5/5".format(r.id))


class TestRectangle_update_args(unittest.TestCase):
    """Tests update() with *args"""

    def test_update_id_only(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_id_width(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual((r.id, r.width), (89, 2))

    def test_update_id_width_height(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual((r.id, r.width, r.height), (89, 2, 3))

    def test_update_all_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_no_args(self):
        r = Rectangle(10, 10)
        original_id = r.id
        r.update()
        self.assertEqual(r.id, original_id)


class TestRectangle_update_kwargs(unittest.TestCase):
    """Tests update() with **kwargs"""

    def test_update_height(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)

    def test_update_multiple_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/10")

    def test_kwargs_ignored_if_args_present(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, x=100)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.x, 10)

    def test_update_unknown_kwarg_ignored_or_set(self):
        r = Rectangle(10, 10)
        r.update(width=5)
        self.assertEqual(r.width, 5)


class TestRectangle_to_dictionary(unittest.TestCase):
    """Tests to_dictionary()"""

    def test_keys(self):
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertEqual(
            set(d.keys()), {"id", "width", "height", "x", "y"})

    def test_values(self):
        r = Rectangle(10, 2, 1, 9, id=5)
        d = r.to_dictionary()
        self.assertEqual(
            d, {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_returns_dict_type(self):
        self.assertIsInstance(Rectangle(1, 1).to_dictionary(), dict)

    def test_update_from_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))


if __name__ == "__main__":
    unittest.main()
