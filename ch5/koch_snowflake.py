'''
koch_snowflake.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Write a function that uses koch() to draw a three-sided
    polygon of Koch curves, also known as a Koch snowflake.
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

def snowflake(t):
    koch(t, 500)
    rt(t, 120)  # turn right 120 degrees
    koch(t, 500)
    rt(t, 120)  # turn right 120 degrees
    koch(t, 500)

snowflake(trtl)   

wait_for_user()
