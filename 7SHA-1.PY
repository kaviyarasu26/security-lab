import hashlib

# Get user input
text = input("Enter the text to calculate SHA-1 message digest: ")

# Calculate SHA-1 hash
sha1_hash = hashlib.sha1(text.encode()).hexdigest()

# Display the result
print("SHA-1 Message Digest:", sha1_hash)