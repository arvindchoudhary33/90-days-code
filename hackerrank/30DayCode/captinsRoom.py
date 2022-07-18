# Based on the application of sets
# input N and a integer list
# ( N representing the repitition of a number in the list)
# Eg:  N = 3 [1,2,2,3,1,2,3,3,1,0]
# so each number is repeted N times
# the number which is/are unique is the output 


n = int(input())
roomNumberList = list(map(int,input().split()))
roomNumberList.sort()

setA = set()
setB = set()

for i in roomNumberList:
    if i in setA:
        setB.add(i)
    else:
        setA.add(i)
setC = list(setA.difference(setB))
print(setC.pop())
