'''
rot_cipher.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Create a function that takes a plaintext string and 
    an integer and encrypts the string by rotating the 
    letters of the string by the integer amount of places.
'''
import string

def rotate_string(s, num):
    crypt = ""
    for ch in s:
        if ch.isupper():
            newCh =  (string.ascii_uppercase.find(ch) + num) % 26
            crypt += string.ascii_uppercase[newCh]
        elif ch.islower():
            newCh =  (string.ascii_lowercase.find(ch) + num) % 26
            crypt += string.ascii_lowercase[newCh]
        else:
            crypt += ch

    return crypt

print rotate_string("...hello!", 13)
