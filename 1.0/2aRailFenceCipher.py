def encrypt_rail_fence(plain_text, rails):
    rail_matrix = [['' for _ in range(len(plain_text))] for _ in range(rails)]
    direction = 1  # 1 for down, -1 for up
    row, col = 0, 0

    for char in plain_text:
        rail_matrix[row][col] = char
        row += direction
        if row == rails or row == -1:
            direction *= -1
            row += 2 * direction
        col += 1

    encrypted_text = ''.join(''.join(row) for row in rail_matrix)
    return encrypted_text

def decrypt_rail_fence(cipher_text, rails):
    rail_matrix = [['' for _ in range(len(cipher_text))] for _ in range(rails)]
    direction = 1  # 1 for down, -1 for up
    row, col = 0, 0

    for char in cipher_text:
        rail_matrix[row][col] = '*'
        row += direction
        if row == rails or row == -1:
            direction *= -1
            row += 2 * direction
        col += 1

    index = 0
    for i in range(rails):
        for j in range(len(cipher_text)):
            if rail_matrix[i][j] == '*':
                rail_matrix[i][j] = cipher_text[index]
                index += 1

    decrypted_text = ''
    row, col = 0, 0
    direction = 1

    for _ in range(len(cipher_text)):
        decrypted_text += rail_matrix[row][col]
        row += direction
        if row == rails or row == -1:
            direction *= -1
            row += 2 * direction
        col += 1

    return decrypted_text

# Get user input
text = input("Enter the text: ")
rails = int(input("Enter the number of rails: "))

# Encrypt and decrypt
encrypted_text = encrypt_rail_fence(text, rails)
decrypted_text = decrypt_rail_fence(encrypted_text, rails)

# Display results
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)