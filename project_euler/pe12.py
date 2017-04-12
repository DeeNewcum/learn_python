#!/usr/bin/env python3

# TODO: this would probably be much faster with a Sieve of Eratosenes (sp?)


import math
import pprint
import sys


# from http://stackoverflow.com/a/22808285/1042525
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def factors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors

def num_factors(n):
    num = 0
    for i in range(1, n+1):
        if n % i == 0:
            num += 1
    return num

#pprint.pprint(factors(28))
#sys.exit()

#print(num_factors(28))
#sys.exit()


tri = 0
for i in range(10000, 10000000):
    tri = math.floor((i*i - i) / 2)
    #numfacs = len(factors(tri))
    numfacs = num_factors(tri)
    if numfacs >= 100:
        print(str(i) + "   (" + str(numfacs) + ")")
    if numfacs > 500:
        print("-----" + i + "------")
        sys.exit()
