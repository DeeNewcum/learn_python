#!/usr/bin/env python3
#
# problem statement:
#
#   A palindromic number reads the same both ways. The largest palindrome made from the product of
#   two 2-digit numbers is 9009 = 91 x 99.
#
#   Find the largest palindrome made from the product of two 3-digit numbers.


max = 1
for x in range(100, 1000):
    for y in range(100, 1000):
        mult = str(x*y)
        revrsed = mult[::-1]            # tricksy, see http://stackoverflow.com/a/931095/1042525
        if mult == revrsed and x*y > max:
            print(x, " * ", y, " = ", mult)
            max = x * y


