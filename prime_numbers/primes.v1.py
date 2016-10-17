#!/usr/bin/env python3
#
# prints a list of primes
#
# confirm by checking against:
#       http://www.bigprimes.net/cruncher/199999/
#       https://www.oeis.org/wiki/Template:Is_prime
#       http://www.tsm-resources.com/alists/prim.html
# 
import pprint           #pprint.pprint(["hello", "world"])
import math

def prime(x):
    for factor in range(2,int(math.sqrt(x))+1):
        if x % factor == 0:
            return False
        #print factor
    return True


ctr = 0
for num in range(2,200001):
    #print num
    if prime(num):
        ctr += 1
        print(ctr, " ", num)

