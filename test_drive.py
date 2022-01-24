from codetimer import Timer

with Timer():
    for i in range(50000000):
        if i%4000000 == 0:
            print(i)
