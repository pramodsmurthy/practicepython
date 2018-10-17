"""
Draw a game board after taking inputs from UserWarning. For 3x3, game board should look like below.

   ---   ---   ---
 |     |     |     |
   ---   ---   ---
 |     |     |     |
   ---   ---   --- 
 |     |     |     |
   ---   ---   ---
   
"""

def draw_game( size ):
    count = 0
    while count < size:
        print("   ---" * size )
        print(" |    " * (size + 1))
        count += 1
    print("   ---" * size )

if __name__ == "__main__":
    size = int(input("Enter the size of game board: "))
    draw_game(size)
