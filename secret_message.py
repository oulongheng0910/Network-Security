
# ==========================================
# TP03 - Task 5: Secret Message Application
# ==========================================

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os


print("================================")
print("     SECRET MESSAGE APP")
print("================================")

# Step 1: Generate AES-128 key
key = AESGCM.generate_key(bit_length=128)

# Step 2: Create AES-GCM object
aes = AESGCM(key)

# Step 3: Generate a fresh nonce
nonce = os.urandom(12)

# Step 4: Ask the user for a message
message = input("\nEnter your secret message: ")

# Convert text into bytes
message_bytes = message.encode("utf-8")

# Step 5: Encrypt the message
ciphertext = aes.encrypt(
    nonce,
    message_bytes,
    None
)

print("\n================================")
print("       ENCRYPTION RESULT")
print("================================")

print("Ciphertext:", ciphertext.hex())

# Step 6: Decrypt the ciphertext
decrypted = aes.decrypt(
    nonce,
    ciphertext,
    None
)

# Step 7: Display original message
print("\n================================")
print("       DECRYPTION RESULT")
print("================================")

print("Original message:", decrypted.decode("utf-8"))

print("\nEncryption and decryption completed!")
