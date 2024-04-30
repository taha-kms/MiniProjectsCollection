import numpy as np
from datetime import datetime as dt
from colorama import init, Fore
init(autoreset=True)


# 9x9 evil sudoku from https://sudoku.com

puzzle = np.array(([[7, 0, 0, 0, 0, 0, 0, 8, 4],
                    [0, 0, 0, 0, 2, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 6, 0, 0, 0],
                    [0, 9, 0, 0, 0, 0, 0, 5, 0],
                    [0, 0, 0, 7, 0, 5, 0, 0, 0],
                    [0, 0, 0, 4, 0, 0, 3, 0, 0],
                    [8, 0, 0, 0, 0, 0, 0, 0, 7],
                    [0, 0, 0, 0, 9, 0, 6, 0, 0],
                    [5, 0, 7, 0, 0, 0, 0, 0, 0]]))


# # ===========================================================================================
# # ===========================================================================================
# # ===========================================================================================

# find location of every empty square individual and return it in tuple.
def find_next_empty(board):

    for i in range(9):
        for j in range(9):
            if board[i, j] == 0:
                return (i, j)

    return None


# # ===========================================================================================
# # ===========================================================================================
# # ===========================================================================================


## checks if the <number> can be plased in the <pos> or not.
def is_valid(board, num, pos):

    ## checking the entire row
    for i in range(9):
        if num == board[pos[0], i]:
            return False

    ## checking the entire column
    for i in range(9):
        if num == board[i, pos[1]]:
            return False


    ## checking the entire square
    square_loc_x = pos[0] // 3
    square_loc_y = pos[1] // 3

    for i in range(square_loc_x * 3, square_loc_x * 3 + 3):
        for j in range(square_loc_y * 3, square_loc_y * 3 + 3):
            if board[i, j] == num:
                return False

    return True


# # ===========================================================================================
# # ===========================================================================================
# # ===========================================================================================


## solves the given sudoku.
def solve_sudo(board: np):

    find = find_next_empty(board)

    ## checks if the puzzle is solved or not.
    if find is None:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            ## backtraking
            if solve_sudo(board):
                return True

            board[row, col] = 0

    return False


# # ===========================================================================================
# # ===========================================================================================
# # ===========================================================================================


## for color the printed number
def colored_number(num):
    if num == 0: return f'{Fore.YELLOW}{num}'
    else :  return f'{Fore.BLUE}{num}'

## for proper look of sudoku view
def print_board(bo):
    for i in range(len(bo)):

        ## at each of squares (row)
        if i % 3 == 0 and i != 0:
            print("")

        ## at each of squares (col)
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("   ", end="")

            ## at end of each row
            if j == 8:
                print(colored_number(bo[i,j]))
            else:
                print(colored_number(bo[i,j]), end="")



print_board(puzzle)
start_time = dt.now()
solve_sudo(puzzle)
print('\n',"===="*20,'\n')
print_board(puzzle)
print(
        f'\nTime of "Solving Sudoku" using < Backtracking algorithem > : {Fore.GREEN}{dt.now() - start_time}\n')

        

