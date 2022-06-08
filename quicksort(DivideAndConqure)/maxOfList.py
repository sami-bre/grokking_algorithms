"""this is a function to find the maximum element of a list by using divide and conqure.
I don't like the idea of removing only the first element to find a smaller problem
(smaller array) for each next recursion, though. maybe there's a better way of doing it."""

def maxOfList(lis):
    if len(lis) == 1:   # base case
        return lis[0]
    else:               # d&c
        maxOfSmallerList = maxOfList(lis[1:])   # this is d&c, baby :)
        if lis[0] > maxOfSmallerList:
            return lis[0]
        else:
            return maxOfSmallerList

print(maxOfList([3,2,5,1]))