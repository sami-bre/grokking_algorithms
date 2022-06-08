def countList(lis, counter=0):
    """counts the number of items in a list and returns the result"""
    if len(lis) == 0:     # base case
        return counter
    else:               # D&C
        lis.pop()
        return countList(lis, counter+1)

# print(countList([3,4,5], 0))


# compare with this code. This is the versiion on the book.

def count(lis):
    if len(lis) == 0:
        return 0
    else:
        lis.pop()
        return 1 + count(lis)

print(count([1,2,3]))