import sys


def methods(string: str) -> None:
    """receives a string and returns boolean depending on wether it meets these conditions: is all caps, is numeric, is ascii or is alphanumeric"""

    print(f"São maiúsculas? {string.isupper()}")
    print(f"É numérico? {string.isnumeric()}")
    print(f"É ascii? {string.isascii()}")
    print(f"É alfanumérico? {string.isalnum()}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        methods(sys.argv[1])
    else:
        print("None")

#  mypy --strict methods.py
