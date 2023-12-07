#!/usr/bin/python3

import re

def validate_username(username):
    """
    Validates if the username matches the necessary format.
    
    Parameters:
    - username (str): The username to validate.
    
    Returns:
    - bool: True if the username is valid, False otherwise.
    """
    # Define a regular expression pattern for username validation
    username_pattern = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')

    # Use the pattern to match the input username
    return bool(username_pattern.match(username))


def validate_password(password):
    """
    Validates if the password matches the necessary format.
    
    Parameters:
    - password (str): The password to validate.
    
    Returns:
    - bool: True if the password is valid, False otherwise.
    """
    # Define your password validation logic here
    # For simplicity, let's just check if the password is at least 8 characters long
    return len(password) >= 8

