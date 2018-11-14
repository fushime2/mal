import unittest
from reader import *

class TestReader(unittest.TestCase):
    def test_Reader(self):
        r = Reader(["(", "+", 1, 1, ")"])
        self.assertEqual(len(r.token), 5)
        self.assertEqual(r.peek(), "(")
        self.assertEqual(r.next(),"(")
        self.assertEqual(len(r.token), 4)
        r.next()
        self.assertEqual(r.next(), 1)
        r.next()
        r.next()
        self.assertEqual(len(r.token), 0)
    
    def test_read_str(self):
        self.fail()
    
    def test_tokenizer(self):
        assert(tokenizer("(+ 1 1)") == ["(", "+", 1, 1, ")"])
        assert(tokenizer("(+ 1 10)") == ["(", "+", 1, 10, ")"])
        assert(tokenizer("(+ 1 (- 0 0))")
            == ["(", "+", 1,"(", "-", 0, 0, ")", ")"])
    
    def test_read_form(self):
        self.fail()
    
    def test_read_list(self):
        self.fail()

    def test_read_atom(self):
        self.fail()

if __name__ == "__main__":
    unittest.main()
