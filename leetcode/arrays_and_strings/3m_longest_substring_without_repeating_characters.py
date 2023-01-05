# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # all types of standard characters you see
        # 0 min length
        sp = 0
        max_total = 0
        total = 0
        ht = {}

        for fp in range(len(s)):
            # encountered unique char
            if ht.get(s[fp]) == None or ht.get(s[fp]) == 0:
                ht[s[fp]] = 1
                total += 1
            else:
                # remove from substring until duplicate is gone
                while sp < fp and ht.get(s[fp]) != 0:
                    ht[s[sp]] = 0
                    sp += 1
                total = fp - sp + 1
                ht[s[fp]] = 1
            
            if total > max_total:
                max_total = total
        
        return max_total