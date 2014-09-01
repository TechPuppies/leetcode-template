# coding=utf-8
# AC Rate: 14.1%
# SOURCE URL: https://oj.leetcode.com/problems/surrounded-regions/
# 
# 
# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# 
# 
# For example,
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# 
# After running your function, the board should be:
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# 


class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        