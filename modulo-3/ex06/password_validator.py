# import sys
import string


def check_password_len(password: str) -> bool:
    """Checks if a given string complies with the password creation rules"""
    return len(password) >= 8 and len(password) <= 16


def check_uppercase(password: str) -> bool:
    return any(char in string.ascii_uppercase for char in password)


def check_lowercase(passwrd: str) -> bool:
    return any(char in string.ascii_lowercase for char in passwrd)


def check_digit(passwrd: str) -> bool:
    return any(char in string.digits for char in passwrd)


def check_punctuation(passwrd: str) -> bool:
    return any(char in string.punctuation for char in passwrd)


def is_valid_password(password: str) -> bool:
    """Checks if a given string complies with the password creation rules"""
    if not check_password_len(password):
        return False
    elif " " in password:
        return False
    elif not check_uppercase(password):
        return False
    elif not check_lowercase(password):
        return False
    elif not check_digit(password):
        return False
    elif not check_punctuation(password):
        return False
    else:
        print("Password is valid")
    return True


# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         print(is_valid_password(sys.argv[1]))
#     else:
#         nl = '\n'
#         print(f"Error: argument missing.{nl}Usage example: python3 password_validator.py <your_password>")
