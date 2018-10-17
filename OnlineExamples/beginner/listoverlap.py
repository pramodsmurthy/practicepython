"""
Compares two lists and outputs a list that has common elements
"""

import random as rn
a = rn.sample(range(1,30), 12)
b = rn.sample(range(1,30), 16) 
newlist = []
[ newlist.append(n1) for n1 in a if n1 in b and n1 not in newlist ]     
print(sorted(newlist))