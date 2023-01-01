# https://leetcode.com/problems/running-sum-of-1d-array/
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sums = []
        running_sum = 0
        for n in nums:
            running_sum += n
            running_sums.append(running_sum)
        return running_sums
