'''
forbidden_letters.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Create a program that reads through a word list and prints
    out the words which do not contain any letters in a 'forbidden'
    string. The word list file and the string of forbiden letters
    are supplied as commandline arguments.
'''
import sys

word_list = open(sys.argv[1])

forbidden = sys.argv[2]

def avoids(wf, frbdn):
    for line in wf:
        avoids = True
        word = line.strip()
        
        for ch in frbdn:
            if ch in word:
                avoids = False

        if avoids:
            print word

avoids(word_list, forbidden)
word_list.close()
