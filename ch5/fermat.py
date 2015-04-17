'''
fermat.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Fermat's Last theorem states that there are no positive integers
    a, b, and c such that

    a^n + b^n = c^n

    for any n > 2.

    More info: https://en.wikipedia.org/wiki/Fermat's_Last_Theorem

    1. Write a function check_fermat that takes four parameters -- a, b, c,
    and n -- and checks to see if Fermat's theorem holds for the values
    provided.
    2. Write a function that prompts the user to input values for a, b, c,
    and n, converts them to integers, and passes them to check_fermat.
'''

def test_theorem():
    values = [ ['a', 0], ['b', 0], ['c', 0], ['n', 0] ] 
    
    for v in values:    # get input and validate
        valid = False
        while not valid:
            v[1] = int(raw_input("Enter a value for %s: " % v[0]))
            if v[0] == 'n' and v[1] <= 2:
                print "n must be greater than 2!"
            elif (v[0] == 'a' or v[0] == 'b' or v[0] == 'c') and v[1] < 1:
                    print "a, b, and c must be positive integers!"
            else:
                valid = True

    check_fermat(values[0][1], values[1][1], values[2][1], values[3][1])

def check_fermat(a, b, c, n):
    if a**n + b**n == c**n:
        print "Fermat was wrong!!"
    else:
        print "Input supports theorem."

test_theorem()
