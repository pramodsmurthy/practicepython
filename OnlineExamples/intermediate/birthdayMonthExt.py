"""
This program displays how many people have birthdays in each month.
"""

from OnlineExamples import birthdayDictsJson as bdj
from collections import Counter

def month_num_to_name(month_num):
    month_num_to_name_match = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December",
    }
    return month_num_to_name_match[month_num]

def count_months(birthdays):
    months = []
    for value in birthdays.values():
        month = month_num_to_name(value.split("-")[0])
        months.append(month)    
    month_count = Counter(months)
    return month_count
        
def main():
    file_location = "C:\\Users\\pkrishna\\eclipse-workspace\\python\\OnlineExPractice\\OnlineExamples\\dicts.json"
    birthdays = bdj.read_file(file_location)    
    month_count = count_months(birthdays)
    print(month_count)

if __name__ == "__main__":
    main()
