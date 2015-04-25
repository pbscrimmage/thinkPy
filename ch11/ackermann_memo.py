'''
ackermann_memo.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Use a dictionary to make the ackermann function more efficient by
    'memo-izing' results of computations, so that results can be retrieved
    from the cache whenever the same inputs are encountered in the 
    recursion tree.
'''
cache = {}

def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    else:
        known = cache.get((m, n), 0)
        if known:
            return known
        else:
            cache[m, n] = ack(m-1, ack(m, n-1))
            return cache[m, n]

print ack(3,8)
