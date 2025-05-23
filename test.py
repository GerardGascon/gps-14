"""
Unit tests for string transformation functions in the transform module.
"""

import unittest
import transform

class TestStringMethods(unittest.TestCase):
    """
    Unit tests for string transformation functions in the transform module.
    """

    def test_is_upper(self):
        """
        Test that to_upper_case correctly converts a lowercase string to uppercase.
        """
        sting = transform.to_upper_case("hello")
        self.assertEqual(sting, "HELLO")

    def test_is_lower(self):
        """
        Test that to_lower_case correctly converts an uppercase string to lowercase.
        """
        sting = transform.to_lower_case("HELLO")
        self.assertEqual(sting, "hello")

    def test_is_capitalize(self):
        """
        Test that to_capitalize correctly capitalizes an uppercase string.
        """
        sting = transform.to_capitalize("HELLO")
        self.assertEqual(sting, "Hello")


if __name__ == '__main__':
    unittest.main()
