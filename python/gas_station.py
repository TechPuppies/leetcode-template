# coding=utf-8
# AC Rate: 25.8%
# https://oj.leetcode.com/problems/gas-station/

# There are N gas stations along a circular route, where the amount of gas at
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
# from station i to its next station (i+1). You begin the journey with an empty
# Return the starting gas station's index if you can travel around the circuit
# Note:
# The solution is guaranteed to be unique.

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        