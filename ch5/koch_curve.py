'''
koch_curve.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Write a function named koch that draws a fractal pattern,
    known as the Koch Curve, with a given length.
    http://en.wikipedia.org/Koch_snowflake

Note:
    Requires Tkinter as well as the swampy package created for use with the book.
    Info here: http://www.thinkpython.com/swampy
'''

from swampy.TurtleWorld import *

world = TurtleWorld()
trtl = Turtle()

def koch(t, length):
    if length < 10:
        fd(t, length)
        return
    koch(t, length/3)
    lt(t, 60)    # turn left 60 degrees
    koch(t, length/3)
    rt(t, 120)  # turn right 120 degrees
    koch(t, length/3)
    lt(t, 60)   # turn left 60 desgrees
    koch(t, length/3)

koch(trtl, 500)

wait_for_user()
