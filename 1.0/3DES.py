from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def generate_key():
    return get_random_bytes(8)

def encrypt_des(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text.encode(), DES.block_size)
    cipher_text = cipher.encrypt(padded_text)
    return cipher_text

def decrypt_des(cipher_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = cipher.decrypt(cipher_text)
    plain_text = unpad(padded_text, DES.block_size)
    return plain_text.decode()

# Get user input
key = generate_key()
text = input("Enter the message to encrypt: ")

# Encrypt and decrypt
encrypted_text = encrypt_des(text, key)
decrypted_text = decrypt_des(encrypted_text, key)

# Display results
print("Key:", key)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)