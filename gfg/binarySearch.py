# Generic Binary Search 
# one of my favorite algorithms ( few lines and O(logn) complexity )

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while(l <= r):
            # NOTE: below line for overflow issue for very large number
            m = l + (r-l) //2

           # m = ( l + r ) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
