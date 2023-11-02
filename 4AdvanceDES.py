from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode

def generate_key():
    return urlsafe_b64encode(os.urandom(32))

def encrypt_aes(plain_text, key):
    key = urlsafe_b64decode(key)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    cipher_text = encryptor.update(plain_text.encode()) + encryptor.finalize()
    return urlsafe_b64encode(iv + cipher_text)

def decrypt_aes(cipher_text, key):
    key = urlsafe_b64decode(key)
    cipher_text = urlsafe_b64decode(cipher_text)
    iv = cipher_text[:16]
    cipher_text = cipher_text[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plain_text = decryptor.update(cipher_text) + decryptor.finalize()
    return plain_text.decode()

# Get user input
key = generate_key()
text = input("Enter the URL to encrypt: ")

# Encrypt and decrypt
encrypted_url = encrypt_aes(text, key)
decrypted_url = decrypt_aes(encrypted_url, key)

# Display results
print("Key:", key)
print("Encrypted URL:", encrypted_url)
print("Decrypted URL:", decrypted_url)