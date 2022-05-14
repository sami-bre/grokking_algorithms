def sum(arr):
    """takes a list of numbers and computes the sum recursively. returns the sum"""
    if len(arr) == 0:   # base case
        return 0
    else:               # divide and conqure
        return arr.pop() + sum(arr)

print(sum([3,5,2,6]))