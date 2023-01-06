# https://leetcode.com/problems/combinations/description/
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        # each subsequent we choose must be > than the last element in our current array
        def generate(arr, n, elements_left_to_pick):
            if elements_left_to_pick == 0:
                results.append(arr)
                return
            
            for i in range(1 if len(arr) == 0 else arr[-1] + 1, n - elements_left_to_pick + 2):
                arr_copy = arr[:]
                arr_copy.append(i)
                generate(arr_copy, n, elements_left_to_pick - 1)

        generate([], n, k)
        return results