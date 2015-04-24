'''
has_no_e.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Create a program that reads words from a word file and prints
    out all words not containing the letter 'e'. Also print out
    the percentage of 'e'-less words.
'''
import sys

word_file = open(sys.argv[1])

def has_no_e(wf):
    '''
    takes a word file argument and prints all
    of the words which dont contain the letter
    'e'. Also prints the percentage of 'e'-less
    words.
    '''
    count = 0
    results = 0
    for line in wf:
        word = line.strip()
        if 'e' not in word:
            results += 1
            print word
        count += 1

    print "Percentage of words without 'e': " + str(results / float(count) * 100)

has_no_e(word_file)
word_file.close()
