"""approaching the knapsack problem with a greedy algorithm that tries to choose
the best item at each step in the hope of optimizing the big solution to the whole problem"""

# items linked with their value/weight ratio.
# for this geedy algorithm, we don't care about their specific value or weight. we just need the ratio
ratio_dict = dict()
ratio_dict[3.33] = ("water", 3)
ratio_dict[3] = ("book", 1)
ratio_dict[4.5] = ("food", 2)
ratio_dict[2.5] = ("jacket", 2)
ratio_dict[6] = ("camera", 1)

# now make a list of all the ratios and sort it.
ratio_list = list()
for key in ratio_dict:
    ratio_list.append(key)

#quicksort
ratio_list.sort(reverse=True)

# solution logic ...
items_to_take = list()
space_left = 6
for ratio in ratio_list:
    if ratio_dict[ratio][1] <= space_left:
        items_to_take.append(ratio_dict[ratio][0])
        space_left -= ratio_dict[ratio][1]
    if space_left == 0:
        break

print(items_to_take)

