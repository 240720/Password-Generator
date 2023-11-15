import random
import string

def generate_password(length):
    # Define possible characters for password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Ensure at least one character of each type in the password
    password_characters = [random.choice(lowercase_letters),
                           random.choice(uppercase_letters),
                           random.choice(digits),
                           random.choice(special_characters)]
    
    # Generate remaining characters for the password
    remaining_length = length - 4
    for _ in range(remaining_length):
        # Randomly select a character category to use for this character
        category = random.choice(["lowercase", "uppercase", "digit", "special"])
        
        # Generate a random character from the selected category
        if category == "lowercase":
            password_characters.append(random.choice(lowercase_letters))
        elif category == "uppercase":
            password_characters.append(random.choice(uppercase_letters))
        elif category == "digit":
            password_characters.append(random.choice(digits))
        else:
            password_characters.append(random.choice(special_characters))
    
    # Shuffle the characters to ensure randomness
    random.shuffle(password_characters)
    
    # Generate the final password by joining the characters
    password = "".join(password_characters)
    
    return password

# Get user input for password length and number of passwords to generate
password_length = int(input("Enter password length (minimum 8): "))
num_passwords = int(input("Enter number of passwords to generate: "))

# Ensure minimum length of 8 characters
if password_length < 8:
    print("Error: Password length must be at least 8 characters.")
else:
    # Generate and print passwords
    for i in range(num_passwords):
        password = generate_password(password_length)
        print(password)
