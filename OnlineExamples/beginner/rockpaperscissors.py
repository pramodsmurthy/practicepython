"""
Rock Paper Scissors Game between 2 players
"""

import sys

a = ["rock", "paper", "scissors", "quit"]
print("Select", end=" ")
print(a)
while True:
    input1 = input("Enter your choice: ")
    input2 = input("Enter your choice: ")
    
    # Sanitize Inputs
    input1 = input1.lower()
    input2 = input2.lower()
    
    # Validate Inputs
    if input1 == a[-1] or input2 == a[-1]:
        sys.exit()
    if input1 not in a or input2 not in a or input1 == input2:
        print("Invalid input. Please enter 'rock' 'paper' 'scissors' or 'quit'. Different inputs for different players ")
        sys.exit()
    
    # Algorithm
    if ( input1 < input2):
        if ( input1 == "paper" and input2 == "scissors"):
            print("%s beats %s. Player 2 is the winner"%(input2, input1))
        else:
            print("%s beats %s. Player 1 is the winner" %(input1, input2))
    else:
        if ( input1 == "scissors" and input2 == "paper"):
            print("%s beats %s. Player 1 is the winner"%(input1, input2))
        else:
            print("%s beats %s. Player 2 is the winner"%(input2, input1))
