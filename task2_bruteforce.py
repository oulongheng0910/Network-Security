
# ==========================================
# TP03 - Task 2: Brute-Force Attack
# ==========================================

def decrypt_caesar(ciphertext, key):
    plaintext = ""

    for letter in ciphertext.upper():
        if letter.isalpha() and letter.isascii():
            # Convert letter to number
            number = ord(letter) - ord('A')

            # Reverse the encryption shift
            decrypted_number = (number - key) % 26

            # Convert number back to a letter
            decrypted_letter = chr(decrypted_number + ord('A'))

            plaintext += decrypted_letter
        else:
            plaintext += letter

    return plaintext


# Intercepted encrypted message
ciphertext = "YMZWXIFD"

print("================================")
print("       BRUTE-FORCE ATTACK")
print("================================")

# Try every possible non-zero key
for key in range(1, 26):
    plaintext = decrypt_caesar(ciphertext, key)

    print("Key", key, ":", plaintext)

print("================================")
print("Total keys tested:", 25)
