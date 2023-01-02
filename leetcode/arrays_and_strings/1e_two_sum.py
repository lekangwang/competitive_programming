# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        indices = [None] * 2
        for i in range(len(nums)):
            match = target - nums[i]
            if ht.get(match) == None:
                ht[nums[i]] = i
            else:
                indices[0] = ht[match]
                indices[1] = i
                break
        return indices 