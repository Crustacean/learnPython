import sys

class recursionlimit:
    def __init__(self, limit):
        self.limit = limit

    def __enter__(self):
        self.old_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)

def fib(n):

    if n < 2:
        return n
    
    return fib(n-1) + fib(n-2)

with recursionlimit(1500):
    print(fib(4))
