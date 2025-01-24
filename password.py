import random
import string

def generate_password(length, complexity):
    # Define character sets based on the complexity level
    if complexity == 'basic':
        characters = string.ascii_lowercase  # a-z
    elif complexity == 'medium':
        characters = string.ascii_letters  # a-z, A-Z
    elif complexity == 'strong':
        characters = string.ascii_letters + string.digits + string.punctuation  # a-z, A-Z, 0-9, special chars
    else:
        print("Invalid complexity level. Defaulting to 'strong'.")
        characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password from the selected characters
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 6:
                print("Password length should be at least 6 characters.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for the length.")
    
    # Get user input for password complexity
    complexity = input("Choose the complexity (basic, medium, strong): ").lower()

    # Generate and display the password
    password = generate_password(length, complexity)
    print(f"Generated password: {password}")

# Run the program
main()
