# memoized fibonnachi

from codetimer import Timer

store = {}

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n in store:
        return store[n]
    else:
        nm2 = fib(n-2)
        nm1 = fib(n-1)
        result = nm2+nm1
        store[n] = result
        return result


print("\nMemoized fibonnachi")
with Timer():
    print(fib(1050))