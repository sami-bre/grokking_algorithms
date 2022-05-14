def binarySearch(lis, item, start, end):
    """does a binary search recursively and returns the index of the item if present. otherwise None.
    start and end are the indices for the scope of the search. the scope shirnks with each recursion.
    that's D&C."""
    if start == end:        # base case
        return start if lis[start] == item else None
    else:                   # d&c
        mid = (start+end)//2
        if lis[mid] < item:
            return binarySearch(lis, item, mid+1, end)
        else:
            return binarySearch(lis, item, start, mid)

print(binarySearch([2,4,5,7,9], 4, 0, 4))
