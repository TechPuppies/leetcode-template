# coding=utf-8
# AC Rate: 27.9%
# SOURCE URL: https://oj.leetcode.com/problems/valid-sudoku/
# 
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# 
# 
# A partially filled sudoku which is valid.
# 
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
# 
# 


class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        