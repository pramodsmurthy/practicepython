"""
This program randomly picks a word from another file swopods.txt
"""

import random
def pick_word( file_location ):
    # Find the number of lines in the file
    with open(file_location) as fh:
        lines = fh.readlines()        
        count = len(lines) 
        fh.close()
    print(count)
    
    # Randomly choose a line number
    line_num = random.randint(0, count)
    
    # Select a word at random line    
    with open(file_location) as fh:
        line = fh.readline()
        cnt = 0
        while cnt <= line_num:
            cnt += 1
            line = fh.readline()
        fh.close()
    word = line.strip("\n")
    print("Word is {0} its length is {1}".format(word, len(word)))
    return word

def main():
    file_location = "C:\\Users\\pkrishna\\eclipse-workspace\\python\\OnlineExPractice\\OnlineExamples\\sowpods.txt"
    pick_word(file_location)
    
if __name__ == "__main__":
    main()


