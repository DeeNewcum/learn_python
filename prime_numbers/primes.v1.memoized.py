#!/usr/bin/env python3
#
# prints a list of primes
#
# This tries to use memoization to speed things up, but it appears to have slowed things down.
# I'm not sure what went wrong.
#
# confirm by checking against:
#       http://www.bigprimes.net/cruncher/199999/
#       https://www.oeis.org/wiki/Template:Is_prime
#       http://www.tsm-resources.com/alists/prim.html
# 
import pprint           #pprint.pprint(["hello", "world"])
import math
import functools

@functools.lru_cache(maxsize=None)        # memoize
def prime(x):
    for factor in range(2,int(math.sqrt(x))+1):
        if prime(factor) and x % factor == 0:
            return False
        #print factor
    return True


ctr = 0
for num in range(2,200001):
    #print num
    if prime(num):
        ctr += 1
        print(ctr, " ", num)


print("prime() memoization -- ", prime.cache_info())
