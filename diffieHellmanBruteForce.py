# Agreed on primitive root A and prime p
# We are Alice (A) and we have private key XA
# We want to communicate with Bob (B) who has XB

# Diffie Hellman key exchange

# Calculate public key YA using private key 
# YA = A^(XA) mod p

# Give YA to Bob
# Bob gives YB to Alice
# Bob worked out YB the same way
# YB = A^(XB) mod p

# Calculate session key 
# KAB = YB^(XA) mod p

# Given insecure small prime
# p = 11, A = 2
# We are Alice with XA = 6
# Bob gave us YB = 3
# Work out XB from this equation: YB = A^(XB) mod p

p = 11
A = 2

for i in range(1,11):
    result = A**(i) % p
    print("test XB = " + str(i) + "; " + "YB= " + str(result))

