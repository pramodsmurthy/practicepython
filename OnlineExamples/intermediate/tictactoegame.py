"""
Program for tic tac toe game between 2 players. Program can scale to any size of drawing board.
"""
import sys

def draw_gameboard( size, matrix ):
    count = 0
    dashes = "   ---"
    pipes = "  "+"|"+"  "
    col_nos = range(0, size)
    while count < size:
        for _ in col_nos:
            print(dashes, end="")
        print()
        for i in col_nos:
            print(pipes + matrix[count][col_nos[i]], end = "")
        print(pipes)
        count += 1
    print(dashes * size )
    
def validate_inputs( row, col, input_count, matrix, size ):
    retValue = False    
    if row < 0 or row > size-1 or col < 0 or col > size-1:
        print("Invalid row / column number")
    elif input_count >= (size * size):
        print("All boxes are filled, cannot take anymore inputs, no winners for this game")
        draw_gameboard(size, matrix)
        sys.exit()
    elif matrix[row][col] != "-":
        print("Invalid location (row/col is invalid). Try a different point")
    else:
        retValue = True        
    return retValue

def initialize_gameboard( size ):
    matrix = []    
    for _ in range(size):
        matrix.append(["-"] * size)
    return matrix                      
            
def check_for_row_hits( size, matrix, player_sym):
    for row in range(size):
        row_win = False                
        for col in range(size-1):
            # Check for rows                           
            if (matrix[row][col] == matrix[row][col+1] == player_sym):
                if ( col == 0 ):
                    row_win = True                    
            else:
                row_win = False                                                        
        if row_win:              
            break
    return row_win

def check_for_col_hits( size, matrix, player_sym):
    for col in range(size):
        col_win = False
        for row in range(size-1):                                
            if (matrix[row][col] == matrix[row+1][col] == player_sym):
                if row == 0:
                    col_win = True
            else:
                col_win = False
        if col_win:            
            break
    return col_win

def check_for_diag_hits( size, matrix, player_sym):
    diag_win1 = False
    diag_win2 = False
    for row in range(size):
        if matrix[row][size-1-row] == player_sym:
            if row == 0:
                diag_win1 = True
        else:
            diag_win1 = False
                            
        if matrix[row][row] == player_sym:
            if row == 0:
                diag_win2 = True
        else:
            diag_win2 = False
    return diag_win1 or diag_win2

def find_winner( matrix, size, players ):    
    for player_sym in range(2):        
        if player_sym == 0:
            player_sym = "X"
        else:
            player_sym = "O"
        
        # Check for row hits
        row_win = check_for_row_hits( size, matrix, player_sym )        
        
        # Check all Column Hits
        col_win = check_for_col_hits( size, matrix, player_sym )         
        
        # Check for Diagonal Hits
        diag_win = check_for_diag_hits( size, matrix, player_sym)            
            
        if row_win is True or col_win is True or diag_win is True:              
            print("Congratulations {0}!!\nYou won! ".format(players[0] if player_sym == "X" else players[1]))
            draw_gameboard(size, matrix)
            return True
        
    return False

def start_game(matrix, size, players):
    input_count = 0
    while True:
        while True:            
            input1 = input("Enter row/col location for player1 ")        
            row = int(input1.split(",")[0]) - 1
            col = int(input1.split(",")[1]) - 1        
            if ( validate_inputs(row, col, input_count, matrix, size) ):
                matrix[row][col] = "X"
                input_count += 1
                draw_gameboard(size, matrix)
                if ( find_winner(matrix, size, players) or input_count == (size * size) ):
                    sys.exit()
                break        
    
        while True:
            input1 = input("Enter row/col location for player2 ")        
            row = int(input1.split(",")[0]) - 1
            col = int(input1.split(",")[1]) - 1
            if ( validate_inputs(row, col, input_count, matrix, size) ):
                matrix[row][col] = "O"
                input_count += 1
                draw_gameboard(size, matrix)
                if (find_winner(matrix, size, players) or input_count == (size * size)):
                    sys.exit()
                break                
                                
def main():
    players = []
    players.append(input("Enter name of player1: ").title())
    players.append(input("Enter name of player2: ").title())
    size = int(input("Enter the size of game board: "))    
    matrix = initialize_gameboard(size)
    draw_gameboard( size, matrix )
    matrix = start_game(matrix, size, players)

if __name__ == "__main__":
    main()