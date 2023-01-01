# https://leetcode.com/problems/find-pivot-index/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # find total sum of all elements
        # scan left to right, subtracting from total and adding to left sum
        right_sum, left_sum = 0, 0 
        pivot = -1
        for n in nums:
            right_sum += n
        
        for i in range(len(nums)):
            if i > 0:
                left_sum += nums[i - 1]
            right_sum -= nums[i]

            if left_sum == right_sum:
                pivot = i
                break
                
        return pivot