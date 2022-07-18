# Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting
# the maximum number of consecutive 's in 's binary representation. When working with different bases
# , it is common to show the base as a subscript.



# NOTE: My solution
#!/bin/python3

import math
import os
import random
import re
import sys


def decToBin(x):
    return list(bin(x)[2:])

def countConsecutiveOnes(binaryNum):
    countOne = []
    count = 0
   # 1 1 1 1 0 1 1 0 1 1 1  
   # 0 1 2 3 4 5 6 7 8 9 10
    for i in range(len(binaryNum)):
        if(binaryNum[i] == '1'):
            count +=1
            #print(i)
        else:
            countOne.append(count)
            count = 0
            #print("NOT :",i)
    countOne.append(count)
    #print(countOne)
    return max(countOne)

if __name__ == '__main__':
    n = int(input().strip())
    binaryNum = decToBin(n)
    maxOnes = countConsecutiveOnes(binaryNum)
    print(maxOnes)




 # NOTE: Solution found on internet

 def find_max_ones(num):
    if not num:
        return 0
    bin_num = bin(num)[2:]
    print(bin_num)
    # it's very pythonic ( easy but did not understand entirely ) 
    return len(max(bin_num.replace('0', ' ').split(), key=len))


if __name__ == '__main__':
    num = int(input('Enter integer number:'))
    max_ones = find_max_ones(num)
    print(max_ones)

