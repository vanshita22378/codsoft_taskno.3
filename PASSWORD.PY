

import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."
    letters = string.ascii_letters  
    digits = string.digits        
    symbols = string.punctuation     
    all_chars = letters + digits + symbols
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input! Please enter a number.")
main()
