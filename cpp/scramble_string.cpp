// coding=utf-8
// AC Rate: 22.7%
// https://oj.leetcode.com/problems/scramble-string/

// Given a string s1, we may represent it as a binary tree by partitioning it to
// Below is one possible representation of s1 = "great":
//     great
//    /    \
//   gr    eat
//  / \    /  \
// g   r  e   at
//            / \
//           a   t
// To scramble the string, we may choose any non-leaf node and swap its two
// For example, if we choose the node "gr" and swap its two children, it produces
//     rgeat
//    /    \
//   rg    eat
//  / \    /  \
// r   g  e   at
//            / \
//           a   t
// We say that "rgeat" is a scrambled string of "great".
// Similarly, if we continue to swap the children of nodes "eat" and "at", it
//     rgtae
//    /    \
//   rg    tae
//  / \    /  \
// r   g  ta  e
//        / \
//       t   a
// We say that "rgtae" is a scrambled string of "great".
// Given two strings s1 and s2 of the same length, determine if s2 is a scrambled

class Solution {
public:
    bool isScramble(string s1, string s2) {
        
    }
};