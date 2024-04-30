import numpy as np
from datetime import datetime as dt
from colorama import init, Fore
init(autoreset=True)


# # ===========================================================================================
# # ===========================================================================================
# # ===========================================================================================


## Every knight valid move in x and y Axis on chess board
move_x = [2, 1, -1, -2, -2, -1,  1,  2]
move_y = [1, 2,  2,  1, -1, -2, -2, -1]


# # ===========================================================================================
# # ===========================================================================================
# # ===========================================================================================


## checks if the move is not outside of the board or the square did not visited.
def validateMove(bo, row, col):
    if row < 8 and row >= 0 and col < 8 and col >= 0 and bo[row, col] == 0:
        return True


# # ===========================================================================================
# # ===========================================================================================
# # ===========================================================================================


## checks if the move is not outside of the board or the square did not visited.
def solve(board, startpoint, counter):

    row , col = startpoint
    ## 8 is for every knight valid move
    for i in range(8):
        if counter >= 65:
            return True

        ## asign new move to the ongoing location of square.
        new_x = row + move_x[i]
        new_y = col + move_y[i]


        if validateMove(board, new_x, new_y):
            board[new_x, new_y] = counter

            ## Backtracking
            if solve(board, (new_x, new_y), counter+1):
                return True
            board[new_x, new_y] = 0
    return False


# # ===========================================================================================
# # ===========================================================================================
# # ===========================================================================================


x = int(input("Enter X: "))
y = int(input("Enter Y: "))

startpoint = (x,y)

board = np.zeros((8, 8))
board[startpoint] = 1
start_time = dt.now()


solve(board, startpoint, 2)
print(f'{Fore.YELLOW}{board.sum()}')
print(f'{Fore.YELLOW}{board}')
print(f'\nTime of "nQueens" using < Backtracking algorithem > : {Fore.GREEN}{dt.now() - start_time}\n')
