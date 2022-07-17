# The program is straight forward, check if two arrays are similar i.e
# 1, 2, 3, 4 is same as 3, 2, 4, 1 also the repitition of numbers must be same
# in both the arrays/list

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        #NOTE: Solution 1 simple & straight-forward
        # trueCounter = True
        # A.sort()
        # B.sort()
        # if(A == B):
        #     return True
        # else:
        #     return False


        #Simple and intuitive solution
        # NOTE: Solution 2 ( by the author itself ) and it's few ms fast than easy one.
        #using a Map to store frequency of elements.
        mp = {}
        #incrementing frequencies of elements present in first array in the Map.
        for i in range (N):
            if A[i] in mp.keys ():
                mp[A[i]] += 1
            else:
                mp[A[i]] = 1

        #decrementing frequencies of elements present in second array in the Map.        
        for i in range (N):
            if B[i] not in mp.keys ():
                return False
            mp[B[i]] -= 1

        for i in mp.keys ():
            #if frequency of any element in Map now is not zero it means that its 
            #count in two arrays was not equal so the arrays are not equal.
            if mp[i] != 0:
                #returning false since arrays are not equal.
                return False

        #returning true if arrays are equal.
        return True

