def solve(board):
    pos = pickEmpty(board)
    if (pos == [-1,-1]):
        return True
    
    #implementing backtracking algorithm. board has to be valid, every time a box is filled. if all possibilities are exhausted
    #box is set to zero, and function solves the previous box with the previous values in the for loop
    for num in range(1,10):
       if (isValid(board,pos,num)):
           board[pos[0]][pos[1]] = num
           if (solve(board)):
               return True

           board[pos[0]][pos[1]] = 0
            
    return False
           
           

def isValid(board, pos, num):

    for i in range(board[0]): #checking if num value exists in row
        if (board[pos[0]][pos[i]] == num) and pos[1] != i:
            return False

    for i in range(len(board)): #checking if num value exists in column
        if (board[i][pos[1]] == num) and pos[0] != i:
            return False    

    #Tim's method
    boxRow = pos[0] // 3
    boxCol = pos[1] // 3

    for i in range(boxCol * 3, boxCol * 3 + 3):
        for j in range(boxRow*3, boxRow*3 + 3):
            if (board[pos[i][j]] == num and pos[0] != i and pos[1] == j):
                return False
    return True                

    
    #my method for checking validity in sub-boxes (will try later)
    '''
    rowInSquare = (pos[0] % 3) + 1
    colInSquare = (pos[1] % 3) + 1

    if rowInSquare == 1: #when num in first row of sub-box
        for i in range(3):
            if (board[pos[0] + 1][pos[1] + i] == num):
                return False
            if (board[pos[0] + 2][pos[1] + i] == num):
                return False
    if rowInSquare == 2: #when num in second row of sub-box
        for i in range(3):
            if (board[pos[0] - 1][pos[1] + i] == num):
                return False
            if (board[pos[0]+ 1][pos[1] + i] == num):
                return False
    else: #when num in third row of sub-box
        for i in range(3):
            if (board[pos[0] - 2][pos[1] + i] == num):
                return False
            if (board[pos[0] - 1][pos[1] + i] == num):
                return False
    '''



    

            

def pickEmpty(board): #finding an empty square
    emptySquare = [-1,-1]

    for i in range(len(board)):
        for j in range (len(board[i])):

            if board[i][j] == 0:
                emptySquare = [i,j] #i opted for lists instead of sets
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



        

    
    

    


        

    



