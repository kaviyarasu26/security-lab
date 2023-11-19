def generate_playfair_matrix(key):
    key = key.replace("J", "I")
    key = key.upper()
    matrix = [['' for _ in range(5)] for _ in range(5)]
    chars = set()

    # Fill matrix with key
    i, j = 0, 0
    for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in chars:
            matrix[i][j] = char
            chars.add(char)
            j += 1
            if j == 5:
                j = 0
                i += 1

    return matrix

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(plain_text, matrix):
    cipher_text = ''
    for i in range(0, len(plain_text), 2):
        char1, char2 = plain_text[i], plain_text[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            cipher_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            cipher_text += matrix[row1][col2] + matrix[row2][col1]

    return cipher_text

def playfair_decrypt(cipher_text, matrix):
    plain_text = ''
    for i in range(0, len(cipher_text), 2):
        char1, char2 = cipher_text[i], cipher_text[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            plain_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plain_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plain_text += matrix[row1][col2] + matrix[row2][col1]

    return plain_text

# Get user input
key = input("Enter the key: ")
plain_text = input("Enter the plain text: ")

# Generate Playfair matrix
playfair_matrix = generate_playfair_matrix(key)

# Encrypt and decrypt
cipher_text = playfair_encrypt(plain_text, playfair_matrix)
decrypted_text = playfair_decrypt(cipher_text, playfair_matrix)

# Display results
print("Encrypted text:", cipher_text)
print("Decrypted text:", decrypted_text)