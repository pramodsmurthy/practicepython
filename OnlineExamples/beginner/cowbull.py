"""
Program to play Cow-Bull Game. 
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, 
they have a cow. For every digit the user guessed correctly in the wrong place is a bull. Every time the user makes a guess,
tell them how many cows and bulls they have. Once the user guesses the correct number, the game is over. Keep track of the number of 
guesses the user makes throughout teh game and tell the user at the end.
"""

import random
import string

def CowGame():
    rand_num = "".join(random.sample(string.digits, 4))
    guess_count = 0
    while True:
        num = input("Guess a number: ")
        guess_count += 1
        cow = 0
        bull = 0
        if rand_num == num:
            print("Great! You guessed it right in %d guesses" %guess_count)
            break    
        for i,n in enumerate(num):
            if rand_num[i] == n:
                cow += 1
            else:
                if n in rand_num:
                    bull += 1
        print("{0} cows, {1} bulls".format(cow,bull))

if __name__ == "__main__":
    CowGame()

                