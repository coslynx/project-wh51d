import logging

class ErrorHandler:
    def __init__(self):
        logging.basicConfig(filename='error.log', level=logging.ERROR)

    def log_error(self, error_message):
        logging.error(error_message)

    def display_error_message(self, error_message):
        print(f"Error: {error_message}")

    def handle_error(self, error_message):
        self.log_error(error_message)
        self.display_error_message(error_message)