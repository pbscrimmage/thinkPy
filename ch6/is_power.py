'''
is_power.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Define a function, is_power, that takes parameters a and b
    and returns True if a is a power of b. Returns False otherwise.
'''

def is_power(a, b):
    if a == b:
        return True
    elif a < b:
        return False
    else:
        return is_power(a/b, b)

print is_power(60, 8)
print is_power(8, 8)
print is_power(64, 8)
