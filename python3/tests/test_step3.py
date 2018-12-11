import unittest
from step3_env import *


class TestStep3(unittest.TestCase):
    def test_EVAL(self):
        self.assertEqual(EVAL(1), 1)
        self.assertEqual(EVAL(["+", 1, 1]), 2)
        self.assertEqual(EVAL(["+", 11, 11]), 22)
        self.assertEqual(EVAL(["+", 1, ["+", 0, 0]]), 1)
        self.assertEqual(EVAL(["+", 1, ["+", 0, ["+", 0, 0]]]), 1)

        self.assertEqual(EVAL(READ("(+ 1 1)")), 2)
        self.assertEqual(EVAL(["+", -1, 1]), 0)
        self.assertEqual(EVAL(READ("(+ -1 1)")), 0)
        self.assertEqual(EVAL(READ("(* -3 6)")), -18)

    def test_eval_ast(self):
        pass

    def test_rep(self):
        self.assertEqual(rep("(+ 1 1)"), "2")
        self.assertEqual(rep("(def! a 114514)"), "114514")
        self.assertEqual(rep("a"), "114514")
        self.assertEqual(rep("(def! b (+ 100 200))"), "300")
        self.assertEqual(rep("b"), "300")

        # let*
        self.assertEqual(rep("(let* (c 1) c)"), "1")




if __name__ == "__main__":
    unittest.main()
