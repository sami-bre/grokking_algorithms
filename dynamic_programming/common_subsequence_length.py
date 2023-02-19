"""using dynamic programming, this code calculates the length of a common subsequence of two strings.
for more on what a subsequence is and how the algorithm works, refer to the book: grokking algorithms."""

def common_subsequence_length(str_one, str_two):
    matrix = [[0 for j in range(len(str_one))] for i in range(len(str_two))]

    def get_element(i, j):
        if i == -1 or j == -1:
            return 0
        return matrix[i][j]
    
    for i in range(len(str_two)):
        for j in range(len(str_one)):
            if str_two[i] == str_one[j]:
                matrix[i][j] = get_element(i-1, j-1) + 1
            else:
                matrix[i][j] = max((get_element(i-1, j), get_element(i, j-1)))
    return matrix[len(str_two)-1][len(str_one)-1]

print(common_subsequence_length("amazing", "damazer"))
