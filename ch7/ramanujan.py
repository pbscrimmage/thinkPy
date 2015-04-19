'''
ramanujan.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Define a function that Uses Ramanujan's infinite series 
    to generate an approximation of pi to within the range of 
    one epsilon. Compare the output of this function to the 
    value stored in math.pi.
'''
import math

epsilon = 1e-15

def estimate_pi(epsilon):
    factor = (2*math.sqrt(2)) / 9801.0
    k = 0
    total = 0
    while True:
        num = math.factorial(4*k) * (1103 + 26390*k)
        den = math.factorial(k)**4 * 396**(4*k)
        term = factor * num / den 
        total += term

        if abs(term) < epsilon:
            break
                
        k += 1

    return 1 / total

print "Ramanujan: " + str(estimate_pi(epsilon))
print "Math module: " + str(math.pi)
