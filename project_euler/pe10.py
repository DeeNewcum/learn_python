#!/usr/bin/env python3
#
# problem statement:
#
#   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#   Find the sum of all the primes below two million.
 

import pprint           #pprint.pprint(["hello", "world"])


# confirm by checking against:
#       https://www.oeis.org/wiki/Template:Is_prime
#       http://www.tsm-resources.com/alists/prim.html
#       http://www.naturalnumbers.org/P-1000.txt
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
        #print(x)
        for y in range(2*x, n+1, x):
            #print(">> ", y)
            sieve[y] = False
    return primes

primes = sieve_of_eratosthenes(2000000)

sum = 0
for prime in primes:
    sum += prime

print(sum)
