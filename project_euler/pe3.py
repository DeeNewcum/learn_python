#!/usr/bin/env python
#
# problem statement:
#
#   The prime factors of 13195 are 5, 7, 13 and 29.
#
#   What is the largest prime factor of the number 600851475143 ?

#import pprint           # pprint.pprint(["hello", "world"])
import math

def is_prime(x):
    for factor in range(2,int(math.sqrt(x))+1):
        if x % factor == 0:
            return False
        #print factor
    return True


sum = 0
factor_me = 600851475143
for factor in range(3, 775147):          # sqrt(600851475143)
    if factor % 3 == 0 or factor % 5 == 0 or factor % 7 == 0:
        next
    if factor_me % factor == 0 and is_prime(factor):
        print factor






