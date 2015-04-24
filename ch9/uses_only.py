'''
uses_only.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Create a program that reads through a word list and prints
    out words which are composed entirely from the letters in 
    a given string. Both the word file and the string of letters
    are given as commandline arguments.
'''
import sys

word_file = open(sys.argv[1])

letters = sys.argv[2]

def uses_only(word, lttrs):
    for ch in word:
        if ch not in lttrs:
            return False
    return True


def uses_only_filter(wf, lttrs):
    for line in wf:
        word = line.strip()
        
        if uses_only(word, lttrs):
            print word

uses_only(word_file, letters)
word_file.close()
