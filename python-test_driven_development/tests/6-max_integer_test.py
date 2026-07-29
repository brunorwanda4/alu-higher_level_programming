#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests the max_integer function"""

    def test_ordered_list(self):
        """Ascending order list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        """Descending order list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """List with a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """No argument uses the default empty list"""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """List with only negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_sign_numbers(self):
        """List with positive and negative numbers"""
        self.assertEqual(max_integer([-10, 0, 10, 5]), 10)

    def test_duplicate_max(self):
        """List with the max value appearing more than once"""
        self.assertEqual(max_integer([4, 4, 2, 1]), 4)

    def test_all_same_value(self):
        """List where every element is identical"""
        self.assertEqual(max_integer([7, 7, 7]), 7)

    def test_floats(self):
        """List of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_max_at_start(self):
        """Max value is the first element"""
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_end(self):
        """Max value is the last element"""
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)


if __name__ == '__main__':
    unittest.main()
