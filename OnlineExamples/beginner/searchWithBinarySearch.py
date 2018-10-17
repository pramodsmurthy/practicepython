"""
Searching for a number in a list using binary search
"""

import random

def binary_search(numlist, num_to_search):
    low = 0
    high = len(numlist) - 1
    iterCount = 0
    while True:
        mid = int ( ( low + high ) / 2)
        iterCount += 1
        if ( numlist[mid] == num_to_search ):
            return True            
        elif ( num_to_search < numlist[mid] ):
            high = mid
        else:
            low = mid
        if ( iterCount == len(numlist) / 2 ):        
            return False            

if __name__ == "__main__":
    numlist = random.sample(range(1, 1000), 50)
    numlist.sort()
    print(numlist)
    num_to_search = int(input("Enter a number to search: "))
    isFound = binary_search(numlist, num_to_search)
    if ( isFound ):
        print("Great! Number {0} is found. ".format(num_to_search))
    else:
        print("Number {0} is not found.".format(num_to_search))

    