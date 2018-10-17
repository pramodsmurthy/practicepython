"""
Guessing Game of numbers
"""

import sys
from numpy import random as ran
numbers = [1,2,3,4,5,6,7,8,9]
randnum = ran.randint(1, 10)
count = 0

while True:
    guessNum = input("Guess the number: ")
    
    #Validate Input value
    if guessNum == "exit":
        print("Quitting the game.")
        sys.exit()
    
    guessNum = int(guessNum)
    if guessNum not in numbers:
        print("Invalid Input. Enter between 1 and 9")
        continue
    
    # Algorithm
    count += 1    
    if guessNum == randnum:
        print("Great!! You guessed it right!. No of Guesses: ", count)
        print("\nLets start a new game")
        count = 0
        randnum = ran.randint(1, 10)
    elif guessNum < randnum:
        print("Guessed it too low, try new guess")
    else:
        print("Guessed it too high, try new guess")        
        