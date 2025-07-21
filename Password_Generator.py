import random
import string

def get_user_input():
    while True:
        try:
            length = int(input("Enter desired password length (min 6): "))
            if length < 6:
                print("⚠Password too short! Try at least 6.")
                continue
            return length
        except ValueError:
            print("Invalid input! Please enter a number.")

def generate_password(length):
    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    all_chars = lowercase + uppercase + digits + symbols
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    return ''.join(password)
def main():
    print(" Welcome to the Secure Password Generator ")
    length = get_user_input()
    password = generate_password(length)
    print(f"\n Your generated password is:\n\n {password}\n")
    print("Tip: Use a password manager to save it securely.")
if __name__ == "__main__":
    main()
