""" Checks if a number is a multiple of 4 or 2.
    Checks if one number divides the other number evenly or not.
"""

num = int( input( "Enter num number: " ) )
check = int( input ("Enter check number ") )
if ( num % 2 == 0 ):
    if ( num % 4 == 0 ):
        print("Number is a multiple of 4 " )
    else:
        print("Number is even " )
else:
    print("Number is odd ")
if ( num % check == 0 ):
    print("%d divides %d evenly " %( check, num ) )
else:
    print("%d does not divide %d evenly " %(check, num ))