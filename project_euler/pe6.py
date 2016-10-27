#!/usr/bin/env python
#import pprint


sum_squares = 0
sum = 0

for i in range(1, 101):
    sum_squares += i*i
    sum += i

print sum*sum - sum_squares
