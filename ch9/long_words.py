'''
long_words.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Create a program that takes a wordlist as input and prints out
    any words that have more than 20 letters.
'''
import sys

word_file = open(sys.argv[1])

def find_big_words(wf):
    '''
    takes a wordlist argument and prints any words
    that have len > 20
    '''
    for line in wf:
        word = line.strip() #remove whitespace
        if len(word) > 20:
            print word

find_big_words(word_file)
word_file.close()
