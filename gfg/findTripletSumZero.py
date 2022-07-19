# Was not able to solve 
# Find triplets from an array/list which sums to zero 
# if any pair exits return True else False

# Niave way would be three loops 
# for i(n-2), for k(n-2), for j(n)
# check a[firstElement] + a[secondElement] + a[thirdElement]  = 0





class Solution:
    def findTriplets(self, arr, n):
        arr.sort()
        sum = 0
        # 0 -1 2 -3 1
        # sorted -> -3, -1, 0, 1, 2
        for i in range(n):
            # left -> -1 secondElement 
            left = i+1
            # right = 2 ( lastElement )
            right = n-1
            while( left < right):
                # arr[i] firstElement
                sum = arr[i] + arr[left] + arr[right]
                if sum == 0:
                    return True
                elif sum > 0:
                    # if the sum is greater, we know
                    # it's a sorted list ( in ascending 1,2,3,4 ) 
                    # so we move right towards the smaller num 
                    right -= 1
                else:
                    # if sum is negative then we move the 
                    # left towards larger num
                    left += 1
        return False
