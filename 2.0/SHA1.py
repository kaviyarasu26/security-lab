import hashlib

def calculate_sha1(input_text):
    sha1_hash = hashlib.sha1(input_text.encode()).hexdigest()
    return sha1_hash

def main():
    user_input = input("Enter the plaintext: ")
    sha1_result = calculate_sha1(user_input)
    
    print(f"SHA-1 Hash of '{user_input}': {sha1_result}")

if __name__ == "__main__":
    main()
