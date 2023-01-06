# https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        # at all times closing_parens_used <= opening_parens_used
        # use recursion to build each string
        def generate(n, s, opening_parens_used, closing_parens_used):
            if opening_parens_used == n and closing_parens_used == n:
                results.append(s)
                return
            
            s_copy = s
            if opening_parens_used < n: 
                s += "("
                generate(n, s, opening_parens_used + 1, closing_parens_used)
            
            if closing_parens_used < opening_parens_used:
                s_copy += ")"
                generate(n, s_copy, opening_parens_used, closing_parens_used + 1)
            
        generate(n, "", 0, 0)
        return results