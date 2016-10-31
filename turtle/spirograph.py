#!/usr/bin/env python3
from turtle import *
from math import *



# https://cs.calvin.edu/courses/cs/106/labs/cs106lab7.html

def formulaX(R, r, p, t):
    return (R+r)*cos(t) - p*cos((R+r)*t/r)

def formulaY(R, r, p, t):
    return (R+r)*sin(t) + p*sin((R+r)*t/r)

def t_iterating(R, r, p):
    t = 2*pi

    up()
    goto(formulaX(R, r, p, t), formulaY(R, r, p, t))
    down()

    while t < 20*pi:    # loop from 2*pi to 20*pi.
        t += 0.05 * pi
        colr = int((t * 255 / (20 * pi)) % 256)
        colr_str = "#%02x%02x%02x" % (255-colr, colr, 255)
        #print(colr_str)
        pencolor(colr_str)

        goto(formulaX(R, r, p, t), formulaY(R, r, p, t))


# radius of the fixed circle
R = 50.0

# radius of the moving circle
r = 45.0

# offset of the pen point, between 10 - 100
p = 100

t_iterating(R, r, p)

done()      # Don't exit right away, otherwise the user won't see the graphics. Wait for the user to close the window.

