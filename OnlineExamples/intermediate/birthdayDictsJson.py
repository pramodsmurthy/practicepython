"""
Program to keep track of birthdays in a json file. Birthdays are read from json file and written to json file when updated.
"""

import json

def read_file(file):
    birthdays= {}
    try:
        with open(file, "r+") as fh:
            birthdays = json.load(fh)
            fh.close()
        return birthdays
    except:
        print("Error reading file '{0}'\nCreating new dictionary".format(file.split("\\")[-1]))
        birthdays = {}
        return birthdays

def write_file(file, birthdays):
    with open(file, "w+") as fh:
        json.dump(birthdays, fh)
        fh.close()

def display_birthdays(file_location, birthdays):
    birthdays = read_file(file_location)
    print("Names and Birthdays stored in your dictionary are:")
    for name,dob in birthdays.items():
        print("{0:15} : {1}".format(name, dob))
    
def main():
    file_location = "C:\\Users\\pkrishna\\eclipse-workspace\\python\\OnlineExPractice\\OnlineExamples\\dicts.json"    
    while True:
        new_birthday = input("Do you want to add birthday to the list ? ")
        if new_birthday in ["yes", "y", "Yes"]:
            name = input("Enter person's name: ").title()
            birthdate = input("Enter {0}'s data of birth: ".format(name))
            birthdays = read_file(file_location)
            birthdays[name] = birthdate
            write_file(file_location, birthdays)
            display_birthdays(file_location, birthdays)                 
        else:
            break

if __name__=="__main__":
    main()