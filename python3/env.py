"""
hold the environment definition
"""


class Env():
    def __init__(self, outer=None):
        self.outer = outer or None
        self.data = {}

    def set(self, k, v):
        self.data[k] = v

    def find(self, k):
        if k in self.data:
            return self
        elif self.outer:
            return self.outer.find(k)
        else:
            return None

    def get(self, k):
        env = self.find(k)
        if not env:
            raise Exception(key + "not found")
        else:
            return env.data[k]
