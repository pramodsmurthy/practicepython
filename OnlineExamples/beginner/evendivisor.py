"""
Prints all the divisors of user's input.
"""

num = int( input ("Enter the number: ") )
num2 = (int(num/2))+1
print(num2)
numlist = range(1, num2)
divisors = [n for n in numlist if num % n == 0 ]
print(divisors)