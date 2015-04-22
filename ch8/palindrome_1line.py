'''
is_palindrome.py

Author: Patrick Rummage

Objective:
    Create a one-line version of a function that tests
    whether a string is a palindrome.
'''
def is_palindrome(s):
    return s == s[::-1]

print is_palindrome("abcddcba")
