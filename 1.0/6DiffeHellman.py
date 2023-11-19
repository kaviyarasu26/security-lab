def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

# Get user input for modulus and base (publicly agreed)
p = int(input("Enter the modulus (p): "))
g = int(input("Enter the base (g): "))

# Get user input for Alice's secret integer (a)
a = int(input("Alice: Enter your secret integer (a): "))

# Calculate A = g^a mod p
A = mod_exp(g, a, p)

# Get user input for Bob's secret integer (b)
b = int(input("Bob: Enter your secret integer (b): "))

# Calculate B = g^b mod p
B = mod_exp(g, b, p)

# Compute shared secret for Alice and Bob
s_alice = mod_exp(B, a, p)
s_bob = mod_exp(A, b, p)

# Display shared secret
print(f"Alice and Bob now share a secret (s): {s_alice} (or {s_bob})")