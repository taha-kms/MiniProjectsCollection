# knight's tour Puzzle

solving knight's tour using backtracking algorithm


## Project status
A knight's tour is a sequence of moves of a knight on a chessboard such that the knight visits every square exactly once. If the knight ends on a square that is one knight's move from the beginning square (so that it could tour the board again immediately, following the same path), the tour is closed (or re-entrant); otherwise, it is open.
This function solves the knight tour problem using Backtracking.
It uses solve() and validateMove() to solve the problem.

It returns false if knight cannot be placed. Given a 8*8 board with the Knight placed on the intended block of an empty board. Moving according to the rules of chess knight must visit each square exactly once. Print the order of each cell in which they are visited.

## What is Backtracking?
Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the time elapsed till reaching any level of the search tree).