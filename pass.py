import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1"
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Loop to generate multiple passwords
while True:
    length = int(input("Enter the password length: "))
    print("Generated password:", generate_password(length))
    
    # Ask the user if they want to generate another password
    again = input("Generate another password? (y/n): ").lower()
    if again != 'y':
        break
