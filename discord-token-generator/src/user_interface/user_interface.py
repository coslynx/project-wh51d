import input_handler
import output_handler
import token_generator
import token_validator

def main():
    username = input_handler.get_username()
    password = input_handler.get_password()

    token = token_generator.generate_token(username, password)

    if token_validator.validate_token(token):
        output_handler.display_token(token)
    else:
        output_handler.display_error("Invalid token generated. Please try again.")

if __name__ == "__main__":
    main()