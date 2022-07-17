# Again a very simple and crazy question
# in this you have to return the number which occurs K times first in the array
# Eg : [1, 2, 3, 2, 1] in this array 1 and 2 occurs two times and k = 2
# answer is  2 becaus 2 occurs first K times ( i.e 2 times )

# I did solve i did everything correct just i did not use one extra if statement
# to break when we got the K times count of a number so because of that i was getting
# 1 again and again and again...


class Solution:
    def firstElementKTime(self,  a, n, k):
        # code here
        # NOTE: solution 1
        b={}
        for i in range(n):
            p=a[i]
            if p in b:
                b[p]+=1
            else:
                b[p]=1
            if b[p]>=k:
                break
        if b[p]>=k:
            return (p)
        else:
           return -1




       # NOTE: solution 2
        # d={}
        # for i in a:
        #     d[i]=0
        # for i in a:
        #     d[i]+=1
        #     if d[i]==k:
        #         return i
        # return -1

