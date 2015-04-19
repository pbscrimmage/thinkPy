'''
repl.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Implement a Read-Eval-Print-Loop using the built-in
    function 'eval'.
'''
import math

def eval_loop():
        read = raw_input(">> ")
        while 'done' not in read:
            try:
                ans = eval(read)
                print ans 
            except Exception, e:
                print "[!!] ERROR: " + str(e)

            read = raw_input(">> ")

        return ans

eval_loop()
