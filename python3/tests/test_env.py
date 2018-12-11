import unittest
from env import *


class TestEnv(unittest.TestCase):
    def test_set(self):
        env = Env()
        self.assertIs(env.find("+"), None)
        env.set("+", lambda a, b: a + b)
        self.assertIsNot(env.find("+"), None)

        self.assertEqual(env.set("a", 114514), 114514)
        self.assertEqual(env.get("a"), 114514)

    def test_find(self):
        pass

    def test_get(self):
        env = Env()
        with self.assertRaises(Exception):
            env.get("+")
        env.set("+", lambda a, b: a + b)
        self.assertEqual(env.get("+")(1, 1), 2)


if __name__ == "__main__":
    unittest.main()
