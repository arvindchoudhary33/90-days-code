# now i understand why these programs are  in basic level
# This program literally took me more than hour ( i know )
# The program is, given two array of size N
# return the Minimum sum of product of each element
# i.e , a[0]*b[0] + a[1]+ b[1]...
# the trick is you can shuffle the elements in both arrays to get
# the sum minimum.
# and you should know one thing which i didn't or my brain stopped working
# when you sort one array in increasing and second array in decreasing
# basically you are multiplying the Big number by small ( which makes sense )
# and see that's soooooooo easy.


class Solution:
    def minValue(self, a, b, n):
        #sorting in ascending order
        a.sort()
        #sorting in descending order
        b.sort(reverse=True)
        tempSum = 0
        for i in range(0,n):
            tempSum +=a[i]*b[i]
        return tempSum


ob = Solution()
minSum = ob.minValue([1,2,3],[1,2,3],3)
print(minSum)



