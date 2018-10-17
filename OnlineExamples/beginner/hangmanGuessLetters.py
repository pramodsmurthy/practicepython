"""
This program asks user to guess all the letters in a word. It throws a message to the user 
if a given letter is present or not. There are no limits on the number of guesses.
"""

def show_word( word ):
    print(word)

def next_letter():
    text = input("Guess the next letter: ")
    if (text == "quit"):
        break
    letter = text[:1].upper()
    return letter

def process_guess(letter, word, user_word):
    for i in range(len(word)):
        if letter == word[i]:            
            user_word = user_word[0:i]+letter+user_word[i+1:]
    return user_word
        
def main():
    word = "EVAPORATE"
    user_word = "---------"
    show_word(user_word)
    while True:
        letter = next_letter()
        user_word = process_guess(letter, word, user_word)        
        show_word(user_word)
        if (word == user_word):
            print("Awesome! You guessed the word")
            break

if __name__ == "__main__":
    main()

