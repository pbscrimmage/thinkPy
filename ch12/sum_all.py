"""
sum_all.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    The built-in function sum takes only two arguments.
    Create a function sumall that takes an arbitrary
    number of arguments and returns their sum.
"""
def sumall(*args):
    total = 0
    for x in args:
        total += x
    return total

print sumall(3,4,5,6)
