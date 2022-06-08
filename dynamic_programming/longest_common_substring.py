"""the longest common substring method uses dynamic programming to calculate, well, the length of the longest
substring two strings have in common."""

def longest_common_string(str_one, str_two):
    grid = list()

    def get_grid_item(i, j):
        if i == -1 or j == -1:
            return 0
        return grid[i][j]

    # make the grid
    for i in range(len(str_one)):
        grid.append([])
        for j in range(len(str_two)):
            grid[i].append(0)
    # fill the grid
    max_len = 0;
    for i in range(len(str_one)):
        for j in range(len(str_two)):
            if str_one[i] == str_two[j]:
                grid[i][j] = get_grid_item(i-1, j-1) + 1
                if grid[i][j] > max_len:
                    max_len = grid[i][j]
            else:
                grid[i][j] = 0

    return max_len


text_one = """After entering the source code and running it a few times, try making
experimental changes to it. The comments marked with (!) have sugges-
tions for small changes you can make. On your own, you can also try to fig-
ure out how to do the following"""

text_two = """You can't run this program from your integrated development environ-
ment (IDE) or editor because it uses the bext module. Therefore, it must be
run from the Command Prompt or Terminal in order to display correctly.
You can find more information about the bext module"""

print(longest_common_string(text_one, text_two))
    