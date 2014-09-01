# coding=utf-8
# AC Rate: 19.9%
# SOURCE URL: https://oj.leetcode.com/problems/evaluate-reverse-polish-notation/
# 
# 
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# 
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
# 
# 
# Some examples:
# 
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
# 
# 
# 


class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        