
# ==========================================
# TP03 - Task 1: Caesar Cipher
# ==========================================

def encrypt_caesar(message, key):
    ciphertext = ""

    for letter in message.upper():
        if letter.isalpha() and letter.isascii():
            # Convert letter to number (A=0, B=1, ..., Z=25)
            number = ord(letter) - ord('A')

            # Shift the letter using modulo 26
            encrypted_number = (number + key) % 26

            # Convert number back to a letter
            encrypted_letter = chr(encrypted_number + ord('A'))

            ciphertext += encrypted_letter
        else:
            ciphertext += letter

    return ciphertext


# Original message
message = "THURSDAY"

# Encryption key
key = 5

# Encrypt message
ciphertext = encrypt_caesar(message, key)

# Display results
print("================================")
print("       CAESAR CIPHER")
print("================================")
print("Plaintext :", message)
print("Key       :", key)
print("Ciphertext:", ciphertext)
