'''
is_triangle.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective: 
    1. Write a function is_triangl that takes three integers as
        arguments, and prints either "yes" or "no" depending on
        whether a triangle may be formed from the given lengths.
    2. Write a function that prompts the user to input three 
        lengths, converts them to integers, and uses is_triangle
        to test whether the given lengths can form a triangle.
'''

def test_lengths():
    values = [ ['a', 0], ['b', 0], ['c', 0] ]  
    
    for v in values:    # get input and validate
        valid = False
        while not valid:
            v[1] = int(raw_input("Enter a value for %s: " % v[0]))
            if v[1] < 1:
                    print "a, b, and c must be positive integers!"
            else:
                valid = True

    is_triangle(values[0][1], values[1][1], values[2][1]) 

def is_triangle(a, b, c):
    var_list = [a, b, c]
    for v in var_list:
        lcopy = var_list[:]
        lcopy.remove(v)
        if v > sum(lcopy):
           print "No." 
    print "Yes."
        
test_lengths()
