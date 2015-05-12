"""
reverse_keys.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Create a function that takes a dictionary and a value
    and returns a list of all keys in the dict that map
    to that value. Return an empty list if there are no
    matches.
"""
def reverse_lookup(d, val):
    results = []
    for k in d:
        if d[k] == val:
            results.append(k)
    return results
