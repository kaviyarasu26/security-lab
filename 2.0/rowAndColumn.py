import numpy as np

plaintext = input("Enter the plain text: ")
key_str = input("Enter the key as number: ")


key = [int(i) for i in key_str]
print(key)

num_rows = (len(plaintext) // len(key)) + 1

Matrix = [['x'] * len(key) for _ in range(num_rows)]

index = 0


for i in range(num_rows):
    for j in range(len(key)):
        if index < len(plaintext):
            Matrix[i][j] = plaintext[index]
            index += 1

Matrix = np.array(Matrix)
Matrix = Matrix.T


result_matrix = np.zeros_like(Matrix, dtype='U1') 
print(result_matrix)
for i, k in enumerate(key):
    result_matrix[k-1] = Matrix[i]


print("Resulting Matrix:")
result=''
for i in result_matrix:
    for j in i:
        result+=j
print(result)
