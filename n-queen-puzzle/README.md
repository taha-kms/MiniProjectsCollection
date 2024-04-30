# n Queen Puzzle

solving nQueen Puzzle using backtracking algorithm


## Project status
The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.
This function solves the N Queen problem using Backtracking.
It mainly uses solve() to solve the problem.

It returns false if queens --> cannot be placed, otherwise return true and placement of queens in the form of 1s. note that there may be more than one solutions, this function prints one of the feasible solutions.

## What is Backtracking?
Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the time elapsed till reaching any level of the search tree).