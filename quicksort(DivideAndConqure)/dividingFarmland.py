"""A good use case of the divide and conqure strategy."""

def divideFarmland(land):
    """takes a land / (width, length) and returns the dimension of the largest squares to divide the land"""
    # get the longerSide ans shorterSide
    if land[0] > land[1]:
        longerSide, shorterSide = land[0], land[1]
    else:
        longerSide, shorterSide = land[1], land[0]

    # base case and recursive case
    if longerSide % shorterSide == 0:
        return shorterSide
    else:
        return divideFarmland((longerSide % shorterSide, shorterSide))


print(divideFarmland((1680, 640)))