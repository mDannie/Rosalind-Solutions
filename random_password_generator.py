import random
import string

# Step 1: Asking User's desired password length
length = int(input("Enter desired password length: "))

# Step 2: Define systemic character pools
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

# Step 3: Pool aggregation
all_characters = letters + digits + special_chars

# Step 4: Iterative password generation
password = ""
for i in range(length):
    password += random.choice(all_characters)

# Step 5: Output
print("Generated Password:", password)