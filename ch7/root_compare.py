'''
root_compare.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Use the previously defined Newtonian sqaure root 
    function and create a function that prints 
    comparisons with the results returned by the sqrt 
    function in the python math module.
'''
import math

def find_root(a, eps):
    appx = a / 2.0
    while True:
        root = (appx + a/appx) / 2

        if abs(appx - root) < eps:
            break
        appx = root
    return root


def compare_loop():
    epsilon = 0.0000001
    for i in range(1, 10):
        myAns = find_root(i, epsilon)
        theAns = math.sqrt(i)
        print str(i) + "\t\t" + str(myAns) + "\t\t" +\
                str(theAns) + "\t\t" + str(abs(myAns - theAns))
        print '\n'

compare_loop()
