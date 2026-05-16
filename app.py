import secrets
import string

def generate_password(length=16, use_symbols=True):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += "!@#$%^&*"

    password = "".join(secrets.choice(characters) for _ in range(length))
    return password

print("Welcome to Password Generator!")
print("-" * 30)

length = int(input("Enter password length (default 16): ") or 16)
symbols = input("Include symbols? (y/n, default y): ").strip().lower() or "y"

password = generate_password(length, use_symbols=(symbols == "y"))

print("-" * 30)
print(f"Your password: {password}")