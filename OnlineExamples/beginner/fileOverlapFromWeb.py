"""
Read two files from web. Find overlapping numbers in both the files
"""

# Read file 1.
# Convert read file to list of numbers.

# Read file 2.
# Convert read file to list of numbers.

# Call a function that finds overlapping numbers and prints them.

import requests

def find_overlap( primenums, happynums):
    commonnums = []
    [commonnums.append(n) for n in primenums if n in happynums]
    print("There are {0} common numbers between both lists. Common Numbers are".format(len(commonnums)))
    print(commonnums)
    
def read_file_from_web(url, local_file_location):
    r = requests.get(url)
    with open(local_file_location, "w+") as fh:
        fh.write(r.text)
        fh.close()    

def string_to_intlist(mylist, file):
    with open(file) as fh:
        line = fh.readline()
        while line:
            mylist.append(int(line))
            line = fh.readline()

if __name__ == "__main__":
    primenums = []
    happynums = []    
    
    # Read from web, copy prime numbers to a local file, convert string of numbers to int and listify the numbers.    
    url = "http://www.practicepython.org/assets/primenumbers.txt"
    local_file_location = "C:\\Users\\pkrishna\\eclipse-workspace\\python\\OnlineExPractice\\OnlineExamples\\readWriteFiles\\primenums.txt"
    read_file_from_web(url, local_file_location)
    string_to_intlist(primenums, local_file_location)    
    
    # Read from web, copy happy numbers to a local file, convert string of numbers to int and listify the numbers.
    url = "http://www.practicepython.org/assets/happynumbers.txt"
    local_file_location = "C:\\Users\\pkrishna\\eclipse-workspace\\python\\OnlineExPractice\\OnlineExamples\\readWriteFiles\\happynums.txt"
    read_file_from_web(url, local_file_location)    
    string_to_intlist(happynums, local_file_location)
    
    find_overlap(primenums, happynums)
    