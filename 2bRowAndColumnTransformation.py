def encrypt_row_column(plain_text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    encrypted_text = ''
    rows = len(key)
    cols = len(plain_text) // len(key)

    if len(plain_text) % len(key) != 0:
        cols += 1

    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    index = 0
    for col in key_order:
        for row in range(rows):
            if index < len(plain_text):
                matrix[row][col] = plain_text[index]
                index += 1

    for row in range(rows):
        encrypted_text += ''.join(matrix[row])

    return encrypted_text

def decrypt_row_column(cipher_text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    decrypted_text = ''
    rows = len(key)
    cols = len(cipher_text) // len(key)

    if len(cipher_text) % len(key) != 0:
        cols += 1

    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    index = 0
    for row in range(rows):
        for col in key_order:
            if index < len(cipher_text):
                matrix[row][col] = cipher_text[index]
                index += 1

    for col in range(cols):
        decrypted_text += ''.join(matrix[row][col] for row in range(rows))

    return decrypted_text

# Get user input
text = input("Enter the text: ")
key = list(map(int, input("Enter the key (e.g., 312): ")))

# Encrypt and decrypt
encrypted_text = encrypt_row_column(text, key)
decrypted_text = decrypt_row_column(encrypted_text, key)

# Display results
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)