"""
Take inputs from two players for tic tac toe game. Player 1 inputs are 'x', player 2 inputs are '0'
"""

import sys

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

def validate_inputs( row, col, input_count, matrix, size ):
    retValue = False
    print(row, col, input_count, size)
    if row < 0 or row > size-1 or col < 0 or col > size-1:
        print("Invalid row / column number")
    elif input_count >= (size * size):
        print("All boxes are filled, cannot take anymore inputs.")
        sys.exit()
    elif matrix[row][col] != "0":
        print("Invalid location (row/col is invalid). Try a different point")
    else:
        retValue = True        
    return retValue

def initialize_matrix( matrix, size ):
    for row in range(size):
        for col in range(size):
            matrix[row][col] = "0"

def take_inputs(matrix, size):
    while True:
        print("Enter inputs in row,column format, Start from 1,1: ")        
        input1 = input("Enter row/col location for player1 ")        
        row = int(input1.split(",")[0]) - 1
        col = int(input1.split(",")[1]) - 1        
        if ( validate_inputs(row, col, input_count, matrix, size) ):
            matrix[row][col] = "X"
            input_count += 1
                                
        input1 = input("Enter row/col location for player2 ")        
        row = int(input1.split(",")[0]) - 1
        col = int(input1.split(",")[1]) - 1
        if ( validate_inputs(row, col, input_count, matrix, size) ):
            matrix[row][col] = "O"
            input_count += 1
        print(input_count, matrix)
                    
if __name__ == "__main__":
    input_count = 0
    size = int(input("Enter the size of matrix: "))
    for mat_ex in range(1):
        matrix = get_input_list(mat_ex)
    initialize_matrix(matrix, size)
    take_inputs(matrix, size)
        
    
    
    
        
        
        
        
        
        
        
    