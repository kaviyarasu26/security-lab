# Initialize an empty 3x3 matrix
matrix = [[0]*3 for _ in range(3)]
print(matrix)

# Populate the matrix with user input
for i in range(3):
    for j in range(3):
        matrix[i][j] = int(input(f"Enter value for position ({i+1}, {j+1}): "))

# Print the matrix
for row in matrix:
    print(row)
