import unittest
from printer import *
from reader import *


class TestPrinter(unittest.TestCase):
    def test_pr_str(self):
        self.assertEqual(pr_str(read_str("123")), "123")
        self.assertEqual(pr_str(read_str("123 ")), "123")
        self.assertEqual(pr_str(read_str("abc")), "abc")
        self.assertEqual(pr_str(read_str("abc ")), "abc")
        self.assertEqual(pr_str(read_str("(123 456)")), "(123 456)")
        self.assertEqual(pr_str(read_str("( 123 456 789 )")), "(123 456 789)")
        self.assertEqual(pr_str(read_str("(+ 1 1)")), "(+ 1 1)")
        self.assertEqual(pr_str(read_str("( + 2 (* 3 4) )")), "(+ 2 (* 3 4))")


if __name__ == "__main__":
    unittest.main()
