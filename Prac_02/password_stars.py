MIN_LENGTH = 6

while True:
    password = input("Enter your password: ")
    if len(password) >= MIN_LENGTH:
        break
    print(f"Password must be at least {MIN_LENGTH} characters. Please try again.")

print("*" * len(password))
