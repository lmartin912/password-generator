import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Secure Password Generator 🔐")
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        if length < 6:
            print("⚠️ Password too short! Setting minimum length to 6.")
            length = 6
    except ValueError:
        print("Invalid input. Using default length 12.")
        length = 12

    password = generate_password(length)
    print(f"\n✅ Generated Password: {password}")

if __name__ == "__main__":
    main()
