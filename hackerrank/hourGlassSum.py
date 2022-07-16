#!/bin/python3

import math
import os
import random
import re
import sys


# was not able to solve

# Found and understood one of the two solutions


# NOTE: Solution 1

def hourGlassSum(arr):
    hourGlassSum=[]
    for i in range(4):
        for j in range(4):
            top = sum(arr[i][j:j+3])
            mid = arr[i+1][j+1]
            bot = sum(arr[i+2][j:j+3])
            hourGlass = top + mid + bot
            hourGlassSum.append(hourGlass)
    return max(hourGlassSum)
if __name__ == '__main__':

    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
maxSum = hourGlassSum(arr)
print(maxSum)





# NOTE: Solution 2


def calculateHourGlassSum(arr, row, col):
    sum=0
    #in this method we add all the 7 indiviual values of the hour glass
    #a 
    sum += arr[row-1][col-1]
    #b
    sum += arr[row-1][col]
    #c
    sum += arr[row-1][col+1]
    #d
    sum += arr[row][col]
    #e
    sum += arr[row+1][col-1]
    #f
    sum += arr[row+1][col]
    #g
    sum += arr[row+1][col+1]

    return sum

if __name__ == '__main__':
    #max sum -63 becoz if we have a hour glass with all -9 we'll get -63
    #so it's like initial or minimum value like ( 0 )
    maxSum = 0
    arr=[]
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    #It's 2D array so two loops
    #We know that it's 6 X 6 array we cannot have hour glass in 
    #last row or column | first row or column so the range (1,5)
    for i in range(1,5):
        for j in range(1,5):
            hourGlassSum = calculateHourGlassSum(arr, i, j)
            if(maxSum < hourGlassSum):
                maxSum = hourGlassSum

    print(maxSum)

