"""
User will have a number in mind (between 0 and 100), system will guess the number.
"""

if __name__ == "__main__":
    count = 0    
    low = 0
    high = 100
    guess_count = 0    
    while guess_count < 50:
        guess_num = int((low + high ) / 2)
        print("System guess is ", guess_num)
        user_guess = int(input("How is the system guess ? (0 - too low, 1 - too high, 2 - right guess): "))
        guess_count += 1
        if user_guess == 2:
            print("System guessed your number right!. It only took {0} guesses".format(guess_count))
            break
        elif user_guess == 0:
            low = guess_num
        else:
            high = guess_num

        