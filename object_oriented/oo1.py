#!/usr/bin/env python3
import pprint           # pprint.pprint(["hello", "world"])


class MyClass:

    def __init__(self, n):
        self.n = n

    def increment(self):
        self.n += 1


x = MyClass(3)
x.increment()
print( x.n )
