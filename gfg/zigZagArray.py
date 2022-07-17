#User function Template for python3
# was not able to solve it,  was easy when you actually understand
# the question
# the mistake i did was not to understand the output and it's pattern properly
class Solution:
    def zigZag(self,arr, n):
        for i in range(len(arr)-1):
            if i % 2 == 0 and arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1], arr[i]
            elif i % 2 == 1 and arr[i] < arr[i+1]:
                arr[i] , arr[i+1] = arr[i+1], arr[i]

obj = Solution()
arr = [1,2,3,4,5]
obj.zigZag(arr, 5)
for i in arr:
    print(i,end=" ")
