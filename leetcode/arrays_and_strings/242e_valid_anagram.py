# https://leetcode.com/problems/valid-anagram/description/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_anagram = True
        unique_chars = 0
        ht = {}
        for ch in s:
            if ht.get(ch) == None:
                ht[ch] = 1
                unique_chars += 1
            else:
                ht[ch] += 1
        
        for ch in t:
            if ht.get(ch) == None:
                is_anagram = False
                break
            ht[ch] -= 1

            if ht[ch] == 0:
                unique_chars -= 1
            elif ht[ch] < 0:
                is_anagram = False
                break
        
        if unique_chars != 0:
            is_anagram = False
        
        return is_anagram