# AC Rate: 19.9%
# SOURCE URL: https://oj.leetcode.com/problems/word-search/
# 
# 
# Given a 2D board and a word, find if the word exists in the grid.
# 
# 
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
# 
# 
# For example,
# Given board = 
# 
# [
#   ["ABCE"],
#   ["SFCS"],
#   ["ADEE"]
# ]
# 
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
# 
# 


class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        