# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for ch in t:
            if index == len(s):
                break
            
            if s[index] == ch:
                index += 1
        
        return index == len(s)