
# ==========================================
# TP03 - Task 4: AES-GCM Encryption
# ==========================================

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os


print("================================")
print("       AES-GCM ENCRYPTION")
print("================================")

# Step 1: Generate AES-128 key
key = AESGCM.generate_key(bit_length=128)

print("\nKey:", key.hex())


# Step 2: Create AES-GCM object
aes = AESGCM(key)


# Step 3: Generate a fresh 12-byte nonce
nonce = os.urandom(12)

print("Nonce:", nonce.hex())


# Step 4: Original message
message = b"My password is 123456"

print("Plaintext:", message.decode())


# Step 5: Encrypt the message
ciphertext = aes.encrypt(
    nonce,
    message,
    None
)

print("\nCiphertext:", ciphertext.hex())


# Step 6: Decrypt the ciphertext
decrypted = aes.decrypt(
    nonce,
    ciphertext,
    None
)

print("\nDecrypted:", decrypted.decode())


# Step 7: Test integrity protection
print("\n================================")
print("       INTEGRITY TEST")
print("================================")

modified = bytearray(ciphertext)

# Change the first byte
modified[0] = modified[0] ^ 1

try:
    decrypted_modified = aes.decrypt(
        nonce,
        bytes(modified),
        None
    )

    print("Decrypted:", decrypted_modified.decode())

except Exception:
    print("WARNING: Message was modified!")
