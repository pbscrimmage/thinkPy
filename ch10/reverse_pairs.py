'''
reverse_pairs.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Create a program that reads through a word list and finds 
    each reverse pair (two valid words that are the reverse of 
    each other).
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
    for w in wl:
        search = find_index(wl, w[::-1])
        if search and wl[search] != w:  #found reverse pair (not palindrome)
            print w + " | " + wl[search] 
            wl.remove(w)  #or else we'll find each pair twice

def main():
    word_file = open(sys.argv[1])

    words = []
    for line in word_file:
        word = line.strip()
        words.append(word)

    word_file.close()

    find_pairs(words)

main()
