# Again straight-forward question
# check if a list can be re-arranged in a way that it might form a arithmetic series
# if yes return True else False

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        diff = []
        arr.sort()
        # List comprehension used
        # for i in range(len(arr)-1):
        #   diff.append(arr[i]-arr[i+1])
        diff = [abs(arr[i] - arr[i+1]) for i in range(len(arr)-1)]
        return (len(set(diff)) <= 1)
