import string
import random

def generate_password(length, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ''
    
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not any([uppercase, lowercase, digits, special_chars]):
        print("Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generation Tool\n")

    # Get user preferences
    length = int(input("Enter the desired length of the password: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate password
    password = generate_password(length, uppercase, lowercase, digits, special_chars)

    # Print the generated password
    if password:
        print("\nGenerated Password: {}".format(password))

if __name__ == "__main__":
    main()
