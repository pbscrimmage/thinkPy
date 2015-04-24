'''
consecutive_doubles.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Create a program that reads through a wordlist and prints out any 
    word that has three consecutive pairs of double letters.
'''
import sys

word_file = open(sys.argv[1])

def has_three_doubles(word):
    i = 0
    while i < len(word)-5:
        if word[i] == word[i+1] and word[i+2] == word[i+3] and \
                word[i+4] == word[i+5]:
            return True
        i += 1
    return False


def find_three_doubles(wf):
    for line in wf:
        word = line.strip()
        if has_three_doubles(word):
            print word

find_three_doubles(word_file)
word_file.close()
