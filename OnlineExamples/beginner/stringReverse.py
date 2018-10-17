"""
Take a string, reverse it and print it
"""

strlist = input("Enter a sentence with multiple words: ")
strlist = " ".join(strlist.split(" ")[::-1])
print(strlist)
#for i in range(len(strlist)):
 #   print( strlist.split() [ len(strlist) - 1 - i ], end=" " )