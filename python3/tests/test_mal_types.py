import unittest
from mal_types import *


class TestTypes(unittest.TestCase):
    def test_is_list(self):
        self.assertTrue(is_list([]))
        self.assertTrue(is_list([1, 1]))
        self.assertFalse(is_list(1))

    def test_is_symbol(self):
        self.assertTrue(is_symbol("+"))
        self.assertTrue(is_symbol("-"))
        self.assertFalse(is_symbol("//"))

    def test_is_number(self):
        self.assertTrue(is_number("0"))
        self.assertTrue(is_number("0.0"))
        self.assertTrue(is_number("1"))
        self.assertTrue(is_number("-1"))
        self.assertTrue(is_number("3.141"))
        self.assertTrue(is_number("-3.141"))
        self.assertFalse(is_number("syamu"))

    def test_is_int(self):
        self.assertTrue(is_int("0"))
        self.assertTrue(is_int("1"))
        self.assertTrue(is_int("-1"))
        self.assertFalse(is_int("0.0"))
        self.assertFalse(is_int("1.1"))
        self.assertFalse(is_int("-1.1"))

    def test_is_float(self):
        self.assertTrue(is_float("0"))
        self.assertTrue(is_float("0.0"))
        self.assertTrue(is_float("1"))
        self.assertTrue(is_float("-1"))
        self.assertTrue(is_float("1.1"))


if __name__ == "__main__":
    unittest.main()
