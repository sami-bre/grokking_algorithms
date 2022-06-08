"""using quicksort (which is an example of D&C to sort an array. The performance of
quicksort depends on the pivot we use. if we always use the largest or smallest element
as a pivot, the runtime will be (n**2) but if we use middle sized elements, it will be O(nlog(n))
even if we use random elements for the pivot, the runtime is O(nlog(n)), says the book."""

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

print(quickSort([3,6,9,4,2,9,5,8,1,9,13,10]))
