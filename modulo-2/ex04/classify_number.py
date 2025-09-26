import sys


def is_positive(number: int) -> bool:
    """receives an integer and returns boolean: True if the number is positive and False otherwise"""
    if number > 0:
        return True
    else:
        return False


if __name__ == "__main__":
    num = int(sys.argv[1])
    print(is_positive(num))

#  mypy --strict classify_number.py
