def solve_sudoku(board, row):

    emptySquare = row.index(0)

    for i in range(1,10):
        
        #if not (i in row) and not i in:
            row[emptySquare] = i

            

def pickEmpty(board): #finding an empty square
    emptySquare = (-1,-1)

    for i in range(len(board)):
        for j in range (len(board[i])):

            if board[i][j] == 0:
                emptySquare = (i,j)
                return emptySquare # row, col

    return emptySquare
    


def printBoard(grid):

    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - -  - - - - - - - - - - -")

        for j in range(grid[i]):
            if j % 3 == 0 and j != 0:
                print("|", end= "")

            if (j == 8):
                print(grid[i][j])
            else:
                print(grid[i][j], end= " ")



        

    
    

    


        

    



