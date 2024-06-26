import random
import string

def generate_password(length):
    if length < 6:
        raise ValueError("Password length must be at least 6 characters.")

    #define character sets 
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    #Ensure the password includes atleast one character from each set
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    #Fill the remaining length with random choices from all characters
    password += random.choices(all_characters, k=length-4)

    #shuffle the same result to ensure randomness
    random.shuffle(password)

    return ''.join(password)

if __name__ == '__main__':
    try: 
        length = int(input("Enter the password length: "))
        print(f"Generated password: {generate_password(length)}")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An error occured: {e}")

