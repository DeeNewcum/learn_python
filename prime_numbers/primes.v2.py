#!/usr/bin/env python
#
# prints a list of primes
#
# confirm by checking against:
#       https://www.oeis.org/wiki/Template:Is_prime
#       http://www.tsm-resources.com/alists/prim.html
#       http://www.naturalnumbers.org/P-1000.txt
# 

import pprint           #pprint.pprint(["hello", "world"])

def sieve_of_eratosthenes(n):
    sieve = [True]*(n+1)
    sieve[0] = False
    sieve[1] = False
    #pprint.pprint(sieve)
    primes = []
    for x in range(2, n+1):
        if not sieve[x]:
            continue
        primes.append(x)
        #print x
        for y in range(2*x, n+1, x):
            #print ">> ", y
            sieve[y] = False
    return primes

primes = sieve_of_eratosthenes(200)

ctr = 0
for x in primes:
    ctr += 1
    print('{0}.  {1}'.format(ctr, x))
