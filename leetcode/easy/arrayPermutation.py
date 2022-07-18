# Very simple program
# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]
# For every value of answerArray is num[num[i]] of first array
# ans[i] = num[num[i]]


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            temp  = nums[nums[i]]
            ans.append(temp)
        return ans
