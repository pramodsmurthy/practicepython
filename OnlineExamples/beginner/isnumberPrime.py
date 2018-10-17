"""
Checks if a given number is prime or not
"""

import sys
def get_divisors( number ):    
    divisorlist = list(range(2, int(number/2)))
    return divisorlist

num = int(input("Enter the number: "))
if num == 1:
    print("Number is not a prime number")
elif num == 2:
    print("Number is a prime number.")
else:
    divisors = get_divisors(num)
    for n in divisors:
        if num % n == 0:
            print("Number %d is not a prime number."%num)
            sys.exit()
print("Number %d is a prime number."%num)