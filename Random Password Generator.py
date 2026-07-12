import random
import string

# Characters (letters + digits)
characters = string.ascii_letters + string.digits

# User se password length lena
length = int(input("Enter Password Length: "))

# Password generate karna
password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:", password)