import unittest
from reader import *


class TestReader(unittest.TestCase):
    def test_Reader(self):
        r = Reader(["(", "+", 1, 1, ")"])
        self.assertEqual(len(r.token), 5)
        self.assertEqual(r.peek(), "(")
        self.assertEqual(r.next(), "(")
        self.assertEqual(len(r.token), 4)
        r.next()
        self.assertEqual(r.next(), 1)
        r.next()
        r.next()
        self.assertEqual(len(r.token), 0)

    def test_read_str(self):
        self.assertEqual(read_str("()"), [])
        self.assertEqual(read_str("(+ 1 1)"), ["+", 1, 1])
        self.assertEqual(read_str("(+ 1 (* 0 0))"), ["+", 1, ["*", 0, 0]])

    def test_tokenizer(self):
        self.assertEqual(tokenizer("(+ 1 1)"), ["(", "+", "1", "1", ")"])
        self.assertEqual(tokenizer("(+ 1 (- 10 0))"),
                         ["(", "+", "1", "(", "-", "10", "0", ")", ")"])
        self.assertEqual(tokenizer(";(+ 1 1)"), [])
        self.assertEqual(tokenizer("~@"), ["~@"])
        self.assertEqual(
            tokenizer("[]{}'`~^@"), [
                "[", "]", "{", "}", "'", "`", "~", "^", "@"])

    def test_read_form(self):
        self.assertEqual(read_form(Reader(tokenizer("()"))), [])
        self.assertEqual(read_form(Reader(tokenizer("(+ 1 1)"))), ["+", 1, 1])
        self.assertEqual(read_form(
            Reader(tokenizer("(+ 1 (* 0 0))"))), ["+", 1, ["*", 0, 0]])

    def test_read_list(self):
        # (+ 1 1)
        r = Reader(["(", "+", "1", "1", ")"])
        self.assertEqual(read_list(r), ["+", 1, 1])

        # (+ 1 (* 0 0))
        r = Reader(["(", "+", "1", "(", "*", "0", "0", ")", ")"])
        self.assertEqual(read_list(r), ["+", 1, ["*", 0, 0]])

    def test_read_atom(self):
        # just a number
        r = Reader(["0"])
        t = read_atom(r)
        self.assertEqual(t, 0)

        r = Reader(["+", "0", "1"])
        t = read_atom(r)
        self.assertEqual(t, "+")


if __name__ == "__main__":
    unittest.main()
