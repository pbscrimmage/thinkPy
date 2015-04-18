'''
palindrome.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Define a function called is_palindrome that takes a string
    argument and returns True if it is a palindrome and False
    otherwise.
'''
import re
import string

test_string = "Are we not drawn onward, we few, drawn onward to new era?"

regex = re.compile('[%s]' % re.escape(string.punctuation))

def is_palindrome(s):
    # remove whitespace and punctuation
    s = s.lower()
    s = s.replace(" ", '')  # get rid of spaces
    s = regex.sub('', s)    # get rid of punct

    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

print is_palindrome(test_string)
