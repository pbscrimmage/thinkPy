'''
abecedarian.py

Author: Patrick Rummage
        [patrickbrumage@gmail.com]

Objective:
    A word is abecedarian if all its letters are in alphabetical
    order. Create a program that reads through a word list and prints
    out all abecedarian words, as well as the total found.
'''
import sys

word_file = open(sys.argv[1])

def is_abecedarian(word):
    i = 0
    while i < len(word)-1:
        if word[i+1] < word[i]:
            return False
        i += 1
    return True

def abeced_filter(wf):
    count = 0
    for line in wf:
        word = line.strip()
        if is_abecedarian(word):
            print word
            count += 1
    
    print "Total abecedarian words: " + str(count)

abeced_filter(word_file)
word_file.close()
