"""
hold the environment definition
"""


class Env():
    def __init__(self, outer=None):
        self.outer = outer or None
        self.data = {}

    def set(self, k, v):
        self.data[k] = v
        return v

    def find(self, k):
        if k in self.data:
            return self
        elif self.outer:
            return self.outer.find(k)
        else:
            return None

    def get(self, k):
        env = self.find(k)
        if env is None:
            raise Exception(k + "not found")
        else:
            return env.data[k]
