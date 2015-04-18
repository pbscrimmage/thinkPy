'''
ackermann.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Write a function named ack that evaluates Ackermann's
    function.
    http://en.wikipedia.org/wiki/Ackermann_function
'''

def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))

print ack(3, 4)
