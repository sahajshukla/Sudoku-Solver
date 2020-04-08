'''
@author = Sahaj Shukla
This is  sudoku solver I'm making because I am quarantined and I am bored.
We will be using the backtrack algorithm to try and make the code work. 
We can also try solving this using RL. However, RL is computationally expensive and kind of an overkill for solving sudoku
'''

board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7],
        ]

# we first define a board_printer function to print the board slightly aesthetically



def solver(board):
    # this is the place where we integrate all the function and actually solve the board
    # we will use recursion in this case and see if the board is already full
    # this works well intuitively, because we are using backtrack algorithm so if all places are already filled, they're also correct
    find = board_finder(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if validating_results(board, i, (row, col)):
            board[row][col] = i
            if solver(board):
                return True
            board[row][col]= 0
    return False


def validating_results(board, number, position):
    for i in range(len(board[0])):
        # we basically want to iterate through every row of a particular column and check if the number has been repeated
        
        if board [position[0]] [i] == number and position[1] != i:
            return False
    
    for i in range(len(board)):
        # we basically want to iterate through every column of a particular row and check if the number has been repeated
        
        if board [i] [position[1]] == number and position[0] != i:
            return False
    
    # checking the boxes is a little tough job. 
    #Intuituvely, however, we can always perform integer division on both the rows and columns to find out what box out of 9 we are in
    box_x = position[0]//3
    box_y = position[1]//3
    
    # here what we do is a little tricky to wrap head around. We will now use the indexes. Simce we have used integer division,
    #we need to again, multiply the numbers with 3 to get the absolute indexes of the block
    
    for i in range(box_x*3, box_x*3+3):
        for j in range(box_y*3, box_y*3+3):
            if board[i][j] == number and (i,j) != position:
                return False
    return True
    
def board_printer(board):
    for i in range(len(board)):
        # let us first provide the row wise separations after every 3 rows
        if i%3 == 0 and i != 0:
            print('-'*12)
        for j in range(len(board[0])):
             if j%3 == 0 and j != 0:
                 print('|', end = "")
             if j == 8:
                 print(board[i][j])
             else:
                 print(str(board[i][j]) +"", end = "")

def board_finder(board):
    # now that we have aesthetically printed the board, Our next step would be to find the empty spaces.
    #We realize that the empty spaces are depicted by 0. So we iterate through the list and find the 0s.
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    
    return None # if all the empty spaces have been filled


# let us finally check how we have faired . We will first see the board before running the solver, then run solver 
# and finally check the solution after solver has been run

print('The board before running the solver')
board_printer(board)
print('\n'*3)
print('__'*20)
solver(board)
print('The board after running the solver')
board_printer(board)