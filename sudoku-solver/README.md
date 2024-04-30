# Sudoku Solver

solving Sudoku Puzzle using backtracking algorithm


## Project status
Sudoku is a logic-based, combinatorial number-placement puzzle. In classic Sudoku, the objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 subgrids that compose the grid contain all of the digits from 1 to 9.
This function solves the Sudoku Puzzle using Backtracking.
It mainly uses solve() to solve and is_valid() to check the right position for the problem.

It returns false if puzzle --> cannot be placed, otherwise return 9X9 numpy array.

## What is Backtracking?
Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the time elapsed till reaching any level of the search tree).