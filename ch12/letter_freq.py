"""
letter_freq.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Create a function called most_frequent that takes a string 
    and returns a list of characters found, sorted by frequency.
"""
import sys

def most_frequent(s):
    freqs = {}
    t = []
    
    for c in s:     # Build dict and count letters
        if c in freqs:
            freqs[c] += 1
        else:
            freqs[c] = 1

    for lttr in freqs:      # Build list of (freq, letter) tuples
        t.append((freqs[lttr], lttr))

    t.sort(reverse=True)    # Sort the letter-tuples by freqf

    res = []        # Creata list of sorted letters
    for freq, lttr in t:
        res.append(lttr)
    
    return res

def main():
    infile = open(sys.argv[1])

    text = ""
    for line in infile:
        text += line.strip()

    frequent = most_frequent(text)
    print ''.join(frequent)

main()
