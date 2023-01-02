# https://leetcode.com/problems/maximum-subarray/description/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # both +ve and -ve integers allowed
        # min array length of 1
        # have a running max, if the prefix is -ve, remove it from our subarray
        max_sum, curr_max_sum = float("-inf"), float("-inf")
        for i in range(len(nums)):
            if curr_max_sum >= 0:
                curr_max_sum += nums[i]
            else:
                curr_max_sum = nums[i]
            
            if curr_max_sum > max_sum:
                max_sum = curr_max_sum
            
        return max_sum