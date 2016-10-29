#!/usr/bin/env python
import pprint
from turtle import *

sides = 6

clear()
screen = Screen()

speed(0)      # 1 = slowest, 6 = normal, 10 = fast, 0 = fastest

for i in range(sides):
    forward(1000 / sides)
    right((360/sides) + 0.5)

done()      # Don't exit right away, otherwise the user won't see the graphics. Wait for the user to close the window.

