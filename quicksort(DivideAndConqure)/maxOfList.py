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