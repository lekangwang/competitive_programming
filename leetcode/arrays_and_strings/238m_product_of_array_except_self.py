# https://leetcode.com/problems/product-of-array-except-self/description/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # both +ve and -ve integers
        # minimum array length 2
        products = [1] * len(nums)  
        prefix, postfix = 1, 1
        for i in range(0, len(nums) - 1):
            prefix *= nums[i]
            products[i + 1] = prefix

        for i in range(len(nums) - 1, 0, -1):
            postfix *= nums[i]
            products[i - 1] *= postfix
        
        return products