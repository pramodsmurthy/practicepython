"""
Check if a given string is a palindrome
"""

isstrpal = input( "Enter a string to test: ")
revstr = isstrpal[::-1]
if ( revstr ==  isstrpal ):
    print("String is a palindrome")
else:
    print("STring is not a palindrome")
      

