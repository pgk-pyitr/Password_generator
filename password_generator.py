import random
import string

def generate_password(length); 
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


