""" 
Prints numbers from a list
"""

arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int( input("Enter number " ) )
print( [ n for n in arr if n < num ] )