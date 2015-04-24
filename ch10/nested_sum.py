'''
nested_sum.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Create a function that iterates through a nested list
    of integers, accumulating the sum.
'''

def nested_sum(nest):
    total = 0
    for item in nest:
        if type(item) == type([]):
            total += nested_sum(item)
        else:
            total += item 
    return total

list1 = []
print nested_sum(list1)

list2 = [1,2,3,4,5]
print nested_sum(list2)

list3 = [[1,2,3],4,5,[6,7,8]]
print nested_sum(list3)

list4 = [ [1,[2,3],4], [[5],[6]], [7,[8,[9]]] ]
print nested_sum(list4)
