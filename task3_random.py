
# ==========================================
# TP03 - Task 3: Randomness in Cryptography
# ==========================================

import random
import secrets

print("================================")
print("   RANDOMNESS IN CRYPTOGRAPHY")
print("================================")

# Exercise 3.1: Predictable randomness
print("\nExercise 3.1: Normal Random")

random.seed(1234)

print("Random value 1:", random.randint(0, 1000000))
print("Random value 2:", random.randint(0, 1000000))
print("Random value 3:", random.randint(0, 1000000))

# Exercise 3.2: Secure randomness
print("\nExercise 3.2: Secure Random")

print("Secure value 1:", secrets.token_hex(16))
print("Secure value 2:", secrets.token_hex(16))
print("Secure value 3:", secrets.token_hex(16))

print("\n================================")
print("Randomness demonstration completed!")