#2D lists
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


# accessing 1 in matrix list
print(matrix[0][0])

# fetching all items using a nested for loop
for row in matrix:
    for item in row:
        print(item)