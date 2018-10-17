"""
Program for Hangman game.
"""

import random

def pick_word( file_location ):
    # Find the number of lines in the file
    with open(file_location) as fh:
        lines = fh.readlines()
        word = lines[random.randint(0, len(lines))].strip("\n")        
        return word

def show_word( word ):
    print(word)

def next_letter():
    text = input("Guess the next letter: ")    
    letter = text[:1].upper()
    return letter

def process_guess(letter, word, user_word, guess_count):
    is_guess_right = False
    for i in range(len(word)):
        if letter == word[i]:            
            user_word = user_word[0:i]+letter+user_word[i+1:]
            is_guess_right = True
    if is_guess_right is False:
        guess_count = guess_count+1         
    return (user_word, guess_count)

def start_game(user_word, word):
    guess_count = 0
    guessed_letters = []    
    while guess_count < 6:
        letter = next_letter()
        if letter in guessed_letters:
            print("Letter {0} already guessed, try a different letter.".format(letter))
            continue        
        guessed_letters.append(letter)
        user_word, guess_count = process_guess(letter, word, user_word, guess_count)
        show_word(user_word)
        if (word == user_word):
            print("Awesome! You guessed the word")
            break
        else:
            print("You have {0} incorrect guesses left".format(6 - guess_count))
            
    if guess_count == 6:
        print("Only 6 guesses allowed per word.. better luck next time!!. Word was ", word)

def main():
    file_location = "C:\\Users\\pkrishna\\eclipse-workspace\\python\\OnlineExPractice\\OnlineExamples\\sowpods.txt" 
    print("Welcome to a game of Hangman.. Good luck!")   
    while True:
        word = pick_word(file_location)
        user_word = "-" * len(word)
        start_game(user_word, word)        
        is_continue = input("Do you want to play another game? Type 'yes' or 'no' ")
        if is_continue == "yes":
            print("Okay, new game then!")
            continue
        else:
            print("Alrighty, good bye!")
            break
    
if __name__ == "__main__":
    main()
