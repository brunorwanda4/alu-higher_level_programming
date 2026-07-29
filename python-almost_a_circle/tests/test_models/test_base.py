#!/usr/bin/python3
"""Unittests for models.base.Base"""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Tests instantiation of the Base class"""

    def test_id_public(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_is_int_type_not_enforced(self):
        b = Base("hello")
        self.assertEqual(b.id, "hello")

    def test_no_id_auto_increments(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_no_id_then_id_given(self):
        b1 = Base()
        b2 = Base(50)
        b3 = Base()
        self.assertEqual(b2.id, 50)
        self.assertEqual(b3.id, b1.id + 1)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Tests Base.to_json_string"""

    def test_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_list_of_dicts(self):
        list_dicts = [{"id": 1}, {"id": 2}]
        json_str = Base.to_json_string(list_dicts)
        self.assertEqual(json.loads(json_str), list_dicts)

    def test_return_type(self):
        self.assertIsInstance(Base.to_json_string([{"id": 1}]), str)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([{"id": 1}], [{"id": 2}])


class TestBase_from_json_string(unittest.TestCase):
    """Tests Base.from_json_string"""

    def test_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_valid_json(self):
        list_dicts = [{"id": 1}, {"id": 2}]
        json_str = json.dumps(list_dicts)
        self.assertEqual(Base.from_json_string(json_str), list_dicts)

    def test_round_trip(self):
        list_dicts = [{"id": 89, "width": 10, "height": 4}]
        json_str = Base.to_json_string(list_dicts)
        self.assertEqual(Base.from_json_string(json_str), list_dicts)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string("[]", "[]")


class TestBase_save_to_file(unittest.TestCase):
    """Tests Base.save_to_file"""

    def tearDown(self):
        for name in ("Rectangle.json", "Square.json", "Base.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_creates_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_file_content(self):
        r1 = Rectangle(10, 7, 2, 8, id=1)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(content, [r1.to_dictionary()])

    def test_save_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_overwrites_existing_file(self):
        r1 = Rectangle(10, 10, id=1)
        Rectangle.save_to_file([r1])
        r2 = Rectangle(2, 2, id=2)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(content, [r2.to_dictionary()])

    def test_square_filename(self):
        s1 = Square(5)
        Square.save_to_file([s1])
        self.assertTrue(os.path.exists("Square.json"))
        self.assertFalse(os.path.exists("Base.json"))

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], [])


class TestBase_create(unittest.TestCase):
    """Tests Base.create"""

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertIsNot(r1, r2)
        self.assertEqual(str(r1), str(r2))

    def test_create_square(self):
        s1 = Square(5, 2, 3, id=10)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertIsNot(s1, s2)
        self.assertEqual(str(s1), str(s2))

    def test_create_returns_correct_type(self):
        r1 = Rectangle(2, 2)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsInstance(r2, Rectangle)
        s1 = Square(2)
        s2 = Square.create(**s1.to_dictionary())
        self.assertIsInstance(s2, Square)


class TestBase_load_from_file(unittest.TestCase):
    """Tests Base.load_from_file"""

    def tearDown(self):
        for name in ("Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_no_file_returns_empty_list(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, id=1)
        r2 = Rectangle(2, 4, id=2)
        Rectangle.save_to_file([r1, r2])
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 2)
        self.assertEqual(str(result[0]), str(r1))
        self.assertEqual(str(result[1]), str(r2))

    def test_load_squares(self):
        s1 = Square(5, id=5)
        s2 = Square(7, 9, 1, id=6)
        Square.save_to_file([s1, s2])
        result = Square.load_from_file()
        self.assertEqual(len(result), 2)
        self.assertEqual(str(result[0]), str(s1))
        self.assertEqual(str(result[1]), str(s2))

    def test_load_returns_new_instances(self):
        r1 = Rectangle(10, 10, id=1)
        Rectangle.save_to_file([r1])
        result = Rectangle.load_from_file()
        self.assertIsNot(result[0], r1)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle.load_from_file(1)


if __name__ == "__main__":
    unittest.main()
