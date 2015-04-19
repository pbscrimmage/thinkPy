'''
common_divisor.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Define a function called gcd that takes positive integer 
    parameters, a and b, and returns their greatest common divisor.
'''

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


print gcd(6, 9)
print gcd(3, 20)
print gcd(8, 12)
