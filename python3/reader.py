import re
class Reader():
    token = []
    def __init__(self, _token):
        self.token = _token

    def next(self):
        assert(len(self.token) > 0)
        return self.token.pop(0);

    def peek(self):
        assert(len(self.token) > 0)
        return self.token[0]

# call tokenizer, and create new Reader obj with the token.
# call read_form with the instance.
def read_str(s):
    return read_form(Reader(tokenizer(s)))

def tokenizer(s):
    pattern = """[\s,]*(~@|[\[\]{}()'`~^@]|"(?:[\\].|[^\\"])*"?|;.*|[^\s\[\]{}()'"`@,;]+)"""
    return [t for t in re.findall(pattern, s) if t[0] != ";"]

def read_form(r):
    """ return mal data type """
    token = r.peek()
    if token == '(':
        return read_list(r)
    else:
        return read_atom(r)

def read_list(r):
    ast = []
    r.next() # => (
    while r.peek() != ")":
        ast.append(read_form(r))

    assert(r.peek() == ")")
    return ast

def read_atom(r):
    t = r.next()
    if t.isdigit(): # number
        return int(t)
    elif t in ["+", "-", "*", "/"]: # symbol
        return t
