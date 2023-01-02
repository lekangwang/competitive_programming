# https://leetcode.com/problems/valid-palindrome/description/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        is_palindrome = True
        while left <= right:
            while left < len(s) - 1 and not s[left].isalnum():
                left += 1
            
            while right > 0 and not s[right].isalnum():
                right -= 1
            
            if left <= right and s[left].lower() != s[right].lower():
                is_palindrome = False
                break
            left += 1
            right -= 1
        return is_palindrome