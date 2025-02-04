import random
import string

def generate_password(length, complexity):
    # Define character sets based on complexity
    char_sets = {
        1: string.ascii_lowercase,                              # lowercase 
        2: string.ascii_letters,                                # Uppercase + lowercase 
        3: string.ascii_letters + string.digits,                # Letters + digits
        4: string.ascii_letters + string.digits + string.punctuation  # Letters + digits + special characters
    }

    
    characters = char_sets.get(complexity, string.ascii_letters)

    # random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Enhanced Password Generator!")
    
    try:
       
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Password length must be at least 1.")
            return

        print("\nSelect the password complexity level:")
        print("1. Lowercase letters only")
        print("2. Uppercase and lowercase letters")
        print("3. Letters and digits")
        print("4. Letters, digits, and special characters")
        complexity = int(input("Enter the complexity level (1-4): "))
        
        if complexity not in range(1, 5):
            print("Invalid complexity level. Please select a value between 1 and 4.")
            return

        password = generate_password(length, complexity)
        print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
