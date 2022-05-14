def quickSort(lis):
    """returns a sorted array afer performing quicksort"""
    if len(lis) < 2:    # base case
        return lis
    else:               # divide and conqure
        pvot = lis[0]
        lowerList = []
        upperList =[]
        for item in lis[1:]:
            if item > pvot:
                upperList.append(item)
            elif item <= pvot:
                lowerList.append(item)
        return quickSort(lowerList) + [pvot,] + quickSort(upperList)

print(quickSort([3,6,4,2,5,8,1,9,13,10]))
