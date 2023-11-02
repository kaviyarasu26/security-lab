import numpy as np

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(26):
        if (a * i) % m == 1:
            return i
    return None

def matrix_mod_inv(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = mod_inverse(det % 26, 26)

    if det_inv is None:
        raise ValueError("Matrix is not invertible.")

    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % 26
    inverse = (det_inv * adjugate) % 26

    return inverse

def prepare_text(text, block_size):
    # Convert text to uppercase and remove non-alphabetic characters
    text = "".join(filter(str.isalpha, text.upper()))

    # Pad the text with 'X' to make its length a multiple of block_size
    while len(text) % block_size != 0:
        text += 'X'

    return text

def text_to_matrix(text, block_size):
    matrix = []
    for char in text:
        matrix.append(ord(char) - ord('A'))

    return np.array(matrix).reshape(-1, block_size)

def matrix_to_text(matrix):
    text = ""
    for row in matrix:
        text += ''.join([chr(char + ord('A')) for char in row])

    return text

def hill_encrypt(plain_text, key_matrix):
    block_size = len(key_matrix)
    prepared_text = prepare_text(plain_text, block_size)
    plain_matrix = text_to_matrix(prepared_text, block_size)

    # Encrypt the plain text
    encrypted_matrix = np.dot(plain_matrix, key_matrix) % 26
    encrypted_text = matrix_to_text(encrypted_matrix)

    return encrypted_text

# Example usage:
key_matrix = np.array([[3, 2], [2, 5]])  # Replace with your own key matrix
plain_text = "HELLO"
encrypted_text = hill_encrypt(plain_text, key_matrix)
print("Plain Text:", plain_text)
print("Encrypted Text:", encrypted_text)
