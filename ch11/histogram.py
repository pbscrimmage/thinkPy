"""
histogram.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Create a function that takes a string and creates 
    a dictionary of letters and their counts. Use the
    dictionary get method to implement it compactly.
"""
def histogram(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

print histogram("brontosaurus")
