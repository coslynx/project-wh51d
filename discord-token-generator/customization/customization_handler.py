import random
import string

def generate_token(length):
    characters = string.ascii_letters + string.digits
    token = ''.join(random.choice(characters) for i in range(length))
    return token

def customize_token_length():
    try:
        length = int(input("Enter the desired token length: "))
        if length <= 0:
            print("Token length must be a positive integer.")
            return None
        return length
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None

def handle_customization():
    length = customize_token_length()
    if length is not None:
        token = generate_token(length)
        print(f"Customized token generated: {token}")

handle_customization()