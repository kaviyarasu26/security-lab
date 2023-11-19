from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend

def generate_keypair():
    private_key = dsa.generate_private_key(
        key_size=1024,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(private_key, message):
    signature = private_key.sign(message.encode(), hashes.SHA256())
    return signature

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(signature, message.encode(), hashes.SHA256())
        return True
    except Exception as e:
        return False

# Get user input
message = input("Enter the message to sign: ")

# Generate keypair
private_key, public_key = generate_keypair()

# Sign the message
signature = sign_message(private_key, message)

# Verify the signature
verification_result = verify_signature(public_key, message, signature)

# Display results
print("Message:", message)
print("Signature:", signature.hex())
print("Verification Result:", verification_result)