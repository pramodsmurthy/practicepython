"""
Takes a list as input, removes dulplicates and displays new list
"""

def remove_list_duplicates_loop( givenlist ):
    newlist = []   
    [newlist.append(n) for i, n in enumerate(givenlist) if n not in givenlist[i+1:] ]    
    return newlist

def remove_list_duplicates_sets( givenlist ):
    return list(set(givenlist))

numbers = input(print("Enter a list of numbers: "))
given_list = numbers.split(" ")
given_list = list(map(float, given_list))
given_list = [int (n) for n in given_list]
newlist = remove_list_duplicates_loop(given_list)
print(newlist)
newlist = remove_list_duplicates_sets(given_list)
print(newlist)