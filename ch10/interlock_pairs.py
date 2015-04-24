'''
interlock_pairs.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Create a program that iterates through a word list
    and finds all pairs of words which 'interlock' to
    form a new word (i.e. 'wide' and 'eros' combine to
    form 'weirdoes').
'''
import bisect
import sys

def find_index(wl, qry):
    index = bisect.bisect_left(wl, qry)
    if index != len(wl) and wl[index] == qry:
        return index
    else:
        return None

def find_pairs(wl):
    count = 0
    for w in wl:
        s1 = w[::2]
        s2 = w[1::2]
        if find_index(wl,s1) and find_index(wl,s2):
            print s1 + " + " + s2 + " = " + w
            count +=1
    print "Pairs found: " + str(count)

def main():
    word_file = open(sys.argv[1])

    words = []
    for line in word_file:
        word = line.strip()
        words.append(word)

    word_file.close()

    find_pairs(words)

main()
