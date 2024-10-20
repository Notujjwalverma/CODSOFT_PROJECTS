import random
import string

def generate_password(length):
    if length < 1:
        return "Invalid length"

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the length of the password you want : "))
print("Generated password:", generate_password(length))
