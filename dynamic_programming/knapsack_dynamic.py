"""
This code is an exaple of dynamic programming. I used dynamic programming to solve 
the famous knapsack problem. The inputs to the problem are hardcoded (that's a bad thing).
I took the problem (and its inputs) directly from the book "grokking algorithms", page 178
, exercise 9.2. I really recommend consulting the book and that excercise to understand the 
code.
"""
from cmath import inf


weights = {1: 3, 2: 1, 3: 2, 4: 2, 5: 1}
values = {1: 10, 2: 3, 3: 9, 4: 5, 5: 6}
letters = {1:'w', 2:'b', 3:'f', 4:'j', 5:'c'}
knapsack_capacity = 6

grid = {
    # each index represents the bag_size
    # each row represents an item
    # this dict has a row and a column of padding (on top and left)
    0:[(0,tuple()) for _ in range(7)],
    1:[(0,tuple()) for _ in range(7)],
    2:[(0,tuple()) for _ in range(7)],
    3:[(0,tuple()) for _ in range(7)],
    4:[(0,tuple()) for _ in range(7)],
    5:[(0,tuple()) for _ in range(7)]
}

def get_previous_estimate(item_id, bag_size):
    return grid[item_id-1][bag_size][0]


def get_item_included_data(item_id, bag_size):
    # if the item can't fit, return 0
    item_weight = weights[item_id]
    if item_weight > bag_size:
        return (0, tuple())
    space_left = bag_size - item_weight
    left_space_data = get_left_space_data(item_id, space_left)
    item_included_value = values[item_id] + left_space_data[0]
    new_item_set = left_space_data[1] + (letters[item_id],)
    return (item_included_value, new_item_set)


def get_left_space_data(item_id, left_space):
    if letters[item_id] not in get_cell_data(item_id, left_space)[1]:
        return get_cell_data(item_id, left_space)
    return get_cell_data(item_id-1, left_space)


def get_cell_data(item_id, bag_size):
    return grid[item_id][bag_size]

for i in range(1,6):
    for j in range(1,7):
        # now i is the item_id whereas j is the bag_size
        current_best_data = get_cell_data(i-1, j)
        item_included_data = get_item_included_data(i, j)
        if item_included_data[0] > current_best_data[0]:
            grid[i][j] = item_included_data
        else:
            grid[i][j] = current_best_data

# this is where the answer to the problem lies.
print(grid[5][6])

