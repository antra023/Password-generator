import random
import string

def generate_password(length):
    """
    Generate a strong, secure password of a given length.

    The password will contain a mix of:
    - Uppercase letters (A-Z)
    - Lowercase letters (a-z)
    - Numbers (0-9)
    - Special characters (!, @, #, $, etc.)

    :param length: The length of the password to generate
    :return: A strong, secure password
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")

    # Get user input for password length and number of passwords
    password_length = int(input("Enter the length of the password: "))
    num_passwords = int(input("Enter the number of passwords to generate: "))

    # Generate and print the passwords
    for i in range(num_passwords):
        password = generate_password(password_length)
        print(f"Password {i+1}: {password}")

if __name__ == "__main__":
    main()