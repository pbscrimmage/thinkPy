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

def uses_only(wf, lttrs):
    for line in wf:
        only = True
        word = line.strip()

        for ch in word:
            if ch not in lttrs:
                only = False

        if only:
            print word

uses_only(word_file, letters)
word_file.close()
