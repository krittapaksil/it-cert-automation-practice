#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        return False
    # Usernames can't begin with a number or should start with a letter
    if not username[0].isalpha():
        return False
    return True

# Example usage:
print(validate_user("john_doe", 5))    # True
print(validate_user("123john", 5))     # False
print(validate_user("mary.jane", 3))   # True
print(validate_user("9lives", 4))      # False
