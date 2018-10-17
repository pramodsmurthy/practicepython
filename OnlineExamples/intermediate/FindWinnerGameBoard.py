"""
This program finds if there is a winner in Tic Tac Toe Game.
"""

def get_input_list( i ):
    if i == 0:
        matrix = [[2, 2, 1],
                 [2, 1, 0],
                 [2, 1, 1]]
    elif i == 1:
        matrix = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 1]]
    elif i == 2:
        matrix = [[0, 1, 0],
                  [2, 1, 0],
                  [2, 1, 1]]
    elif i == 3:
        matrix = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 2]]
    else:
        matrix = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]
    return matrix

def find_winner( matrix, i ):    
    size = 3
    players = 2   
    print(matrix, end=" --- ") 
    for player in range(players):
        player += 1
        diag_win1 = False
        row_win = False
        col_win = False
        diag_win2 = False        

        # Check for row hits
        for row in range(size-1):
            row_win = False                
            for col in range(size-1):
                # Check for rows                           
                if (matrix[row][col] == matrix[row][col+1] == player):
                    if ( col == 0 ):
                        row_win = True                    
                else:
                    row_win = False                                                        
            if row_win:
                print("Matrix {0}: Player {1} is the winner. Row Hit!".format(i, player))  
                break          
        
        # Check all Column Hits
        for col in range(size-1):
            col_win = False
            for row in range(size-1):                                
                if (matrix[row][col] == matrix[row+1][col] == player):
                    if row == 0:
                        col_win = True
                else:
                    col_win = False
            if col_win:
                print("Matrix {0}: Player {1} is the winner. Column Hit!".format(i, player))
                break            
        
        # Check for Diagonal Hits
        diag_win1 = False
        diag_win2 = False
        for row in range(size):
            if matrix[row][size-1-row] == player:
                if row == 0:
                    diag_win1 = True
            else:
                diag_win1 = False
                            
            if matrix[row][row] == player:
                if row == 0:
                    diag_win2 = True
            else:
                diag_win2 = False
        
        if diag_win1 or diag_win2:
            print("Matrix {0}: Player {1} is the winner. Diagonal Hit!".format(i, player))
            
        if row_win is True or col_win is True or diag_win1 is True or diag_win2 is True:
            break
        
        if row_win is False and col_win is False and diag_win1 is False and diag_win2 is False and player == 2:
            print("Matrix {0}: There are no winners.".format(i))
    
                
if __name__ == "__main__":    
    for i in range(5):
        matrix = get_input_list(i)
        find_winner(matrix, i)        