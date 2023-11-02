def encrypt_vigenere(plain_text, key):
    encrypted_text = ""
    key = key.upper()
    key_length = len(key)
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A')
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_vigenere(cipher_text, key):
    decrypted_text = ""
    key = key.upper()
    key_length = len(key)
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A')
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

# Get user input
key = input("Enter the key: ")
plain_text = input("Enter the plain text: ")

# Encrypt and decrypt
encrypted_text = encrypt_vigenere(plain_text, key)
decrypted_text = decrypt_vigenere(encrypted_text, key)

# Display results
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)