"""
has_duplicates.py

Author: Patrick Rummage

Objective:
    Create a function called has_duplicates that uses
    a dictionary to find whether a given list has 
    duplicate items.
"""

def has_duplicates(l):
    found = {}
    for x in l:
        if x in found:
            return True
        else:
            found[x] = 1
    return False

test1 = [0,1,2,4,4,5,6]
test2 = [0,1,2,3,4,5]
test3 = ['a','b','d','e']
test4 = ['a','b','b','e']
test5 = []

print has_duplicates(test1)
print has_duplicates(test2)
print has_duplicates(test3)
print has_duplicates(test4)
print has_duplicates(test5)
