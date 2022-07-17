#Reverse a group of array
#Input -> Array, Size of Array, size of group K 
#If size of array is 17, and K is 5 it means group it in five numbers
# reverse each group numbers and also reverse the group which are left-over 
# i.e ( which do not form five, in this case remaining 2 final digits )
# eg : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] 
# K = 4
# OUTPUT : [4, 3, 2, 1, 9, 8, 7, 6, 13, 12, 11, 10, 14]


# Was not able to solve ( had to watch couple of tutorials to understand )
# though its listed as Level Basic program on the site ( hehe )
# Approach : 
# you keep two pointers one pointing towards the first element
# second towards the Kth element so we get a group K 
# until left < right ( i.e same as binary search )
# we  

class Solution:
#Function to reverse every sub-array group of size k.
 def reverseInGroups(self, arr, N, K):
       i = 0
       while i < len(arr):
           left  = i
           right = min(i + K - 1, len(arr)-1)
           while left < right:
               arr[left], arr[right] = arr[right], arr[left]
               left += 1
               right -= 1
               # And ofcourse i for changing the groups from 1 to 2 to 3..
           i = i + K
       return arr


#Eg [1, 2, 3, 4] ( first group )
# left      Right  ( pointers )
#  1   2 3   4
# swap left to right
# left      Right
#  4   2 3   1
# increment left +1
# decrement right -1
#    left  right 
# 4    2     3    1  
#swap again 
# 4 3 2 1 ( first group done same for remaining )


# 4 2 3 1
# 2 3 

