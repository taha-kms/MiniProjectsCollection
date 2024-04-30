import numpy as np
from datetime import datetime as dt
from colorama import init, Fore
init(autoreset=True)


# # ===========================================================================================
# # ===========================================================================================
# # ===========================================================================================


def validate(board: np, n):

    # checks that if the rows of the board have occupied any queen.
    for row in range(0, n):
        if sum(board[row, ]) > 1:
            return False

    # checks that if the columns of the board have occupied any queen.
    for col in range(0, n):
        if sum(board[:, col]) > 1:
            return False

    # create an array from each from each diagonals of board
    diags = [board[::-1, :].diagonal(i) for i in range(-n+1, n)]
    diags.extend(board.diagonal(i) for i in range(n-1, -n, -1))
    for x in diags:
        if len(x) > 1:
            if sum(x) > 1:
                return False

    # if there was no queens return true
    return True


# # ===========================================================================================
# # ===========================================================================================
# # ===========================================================================================


def solve(board, n, col=0):

    if validate(board, n):
        # checks if the board placed all the needed queens
        if board.sum() == n:
            return True

        for row in range(0, n):
            board[row, col] = 1

            if validate(board, n):
                # checks the next column ( recursive )
                if solve(board, n, col+1):
                    return True

                # if the plasement is worng take the queen and go back
                board[row, col] = 0
            else:
                board[row, col] = 0
    return False


n = int(input('Enter a number: '))
board = np.zeros((n, n))
start_time = dt.now()
if solve(board, n):

    print(f'{Fore.YELLOW}{board}')
    print(
        f'\nTime of "nQueens" using < Backtracking algorithem > : {Fore.GREEN}{dt.now() - start_time}\n')
