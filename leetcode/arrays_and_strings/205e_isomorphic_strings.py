# https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        t_to_s = {}
        s_to_t = {}
        for i in range(len(t)):
            # we've encountered a new character
            if t_to_s.get(t[i]) == None:
                # check if the corresponding character in s is already taken
                if s_to_t.get(s[i]) == None:
                    # create pair
                    t_to_s[t[i]] = s[i]
                    s_to_t[s[i]] = t[i]
                else:
                    return False
            else:
                # check if corresponding character in s matches that in t
                if t_to_s[t[i]] != s[i]:
                    return False
        return True