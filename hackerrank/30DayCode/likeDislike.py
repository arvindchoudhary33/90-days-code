# Easy - This program is about speed of sets
# There are three Array's (Base Array, Array like, Array dislike)
# if anyElement from like array is in BaseArray then likeCounter increases 
# if anyElement from dislike array is in BaseArray then likeCounter decreases
# there are different easy  ways to implement  this but not the efficient
# i did not  look up for the solution but what i did before was use
# some naive for loop while check like /dislike in lists.
# but it failed in few large cases
# I don't know the exact reason behind this program why the sets are fast 
# sets are implemented in python as hashtables and list as dynamic arrays
# searching in hashtable is faster than in dynamic array i suppose

inp = list(map(int, input().split()))
n = inp[0]
m = inp[1]
arr = list(map(int, input().split()))
like = set(map(int, input().split()))
dislike = set(map(int, input().split()))

#makes a little difference
arr.sort()
likeCounter = 0
for i in arr:
    if i in like:
        likeCounter += 1
    if i in dislike:
        likeCounter -= 1
print(likeCounter)
