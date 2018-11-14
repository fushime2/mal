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
    pass

def read_list():
    pass

def read_atom():
    pass
