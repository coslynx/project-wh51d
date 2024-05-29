# Python Discord Token Generator

The Python Discord Token Generator is a tool designed to create unique Discord tokens for users. It provides a user-friendly interface for generating tokens securely and conveniently.

## Features

- Generate Discord tokens based on user input
- Option to save generated tokens for future use
- Customize token length and complexity
- Encrypt user data for security and privacy
- Validate generated tokens to prevent errors or misuse
- Error handling mechanisms for a smooth user experience
- Auto-refresh tokens at specified intervals
- Clear documentation for effective tool usage

## Tech Stack

- Programming Language: Python
- Libraries:
  - discord.py (1.7.3) - For interacting with Discord API
  - pycryptodome (3.11.0) - For encryption techniques
  - pyperclip (1.8.3) - For copying generated tokens

## File Structure

- `src`
  - `user_interface`
    - `input_handler.py`
    - `output_handler.py`
    - `user_interface.py`
  - `token_generator`
    - `token_generator.py`
  - `token_validation`
    - `token_validator.py`
- `encryption`
  - `encryption_utils.py`
  - `encryption_handler.py`
- `customization`
  - `customization_handler.py`
- `error_handling`
  - `error_handler.py`
- `token_auto_refresh`
  - `token_refresh.py`