'''
uses_all.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Create a program that reads through a word list and prints out
    all words which contain all letters in given string. The word file
    and the 'required' string are given as commandline arguments.
        only = True
'''
import sys

word_list = open(sys.argv[1])

required = sys.argv[2]

def uses_all(word, req):
    for ch in req:
        if ch not in word:
            return False
    return True


def uses_all_filter(wf, req):
    for line in wf:
        word = line.strip()
        if uses_all(word, req):
            print word

use_all_filter(word_list, required)
word_list.close()
