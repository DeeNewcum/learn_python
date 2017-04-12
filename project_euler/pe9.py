#!/usr/bin/env python3
import math
import sys
import pprint           # pprint.pprint(["hello", "world"])

for a in range(1, 1001):
    for b in range(a, 1001):
        c = math.sqrt(a*a + b*b)
        if a + b + c == 1000:
            print(a)
            print(b)
            print(a * b * c)
            sys.exit()
            
