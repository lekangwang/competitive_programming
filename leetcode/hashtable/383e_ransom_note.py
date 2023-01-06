# https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ht = {}
        for ch in magazine:
            if ht.get(ch) == None:
                ht[ch] = 1
            else:
                ht[ch] += 1

        for ch in ransomNote:
            if ht.get(ch) == None or ht.get(ch) - 1 < 0: 
                return False 
            else:
                ht[ch] -= 1
            
        return True
        