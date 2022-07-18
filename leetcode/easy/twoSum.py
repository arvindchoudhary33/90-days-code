from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # NOTE: Better solution using hashmap with O(n) complexity
        # prevMap = {}
        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in prevMap:
        #         return [prevMap[diff], i]
        #     prevMap[n] = i



        #NOTE: Brute Force O(n*n) complexity
        for i in range(len(nums)-1):
            for j in range(1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
        return

a = Solution()
solution = list(a.twoSum([1,2,3,4],7))
print(solution)
