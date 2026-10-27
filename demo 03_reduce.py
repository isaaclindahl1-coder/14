"""
the reduce function is used to reduce  a colection into a single value
unlike built in functions like map and filter, the reduce functon is not 
built directly into python
"""
from functools import reduce

grades = [98, 72, 51, 84, 68]

#reduce syntax:
#reduce(function, collection)
def sum(x, y):
    return x + y

total_scores = reduce(sum, grades)
#essentially, it is calling sum(sum(sum(98,))
print(total_scores)
