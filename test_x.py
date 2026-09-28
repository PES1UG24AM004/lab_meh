"""Unit tests for x module using PyUnit (unittest)."""

import unittest
from x import add


class TestAddition(unittest.TestCase):
    """Test cases for addition function with various values for X and Y."""

    def test_positive_numbers(self):
        """Test addition with positive numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)

    def test_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(add(-1, -4), -5)
        self.assertEqual(add(-10, -20), -30)

    def test_mixed_numbers(self):
        """Test addition with mixed positive and negative numbers."""
        self.assertEqual(add(10, -3), 7)
        self.assertEqual(add(-5, 12), 7)

    def test_with_zero(self):
        """Test addition with zero."""
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(7, 0), 7)
        self.assertEqual(add(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
