'''
bisect_search.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Create a program that uses the bisect module to find
    a word in a wordlist using bisection search.
'''
import bisect
import sys

def find_index(wl, qry):
    index = bisect.bisect_left(wl, qry)
    if index != len(wl) and wl[index] == qry:
        return index
    else:
        return None

def main():
    word_file = open(sys.argv[1])
    query = sys.argv[2]

    words = []
    for line in word_file:
        word = line.strip()
        words.append(word)

    word_file.close()
       
    search = find_index(words, query)

    if search:
        print "Found " + query + " at index: " + str(search)
        print words[search]
    else:
        print "Not Found."

main()
