def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def decrypt(ciphertext, shift):
    return encrypt(ciphertext, -shift)

# Example
plaintext = "Hello, Caesar!"
shift_value = 3

# Encryption
encrypted_text = encrypt(plaintext, shift_value)
print("Encrypted:", encrypted_text)

# Decryption
decrypted_text = decrypt(encrypted_text, shift_value)
print("Decrypted:", decrypted_text)
