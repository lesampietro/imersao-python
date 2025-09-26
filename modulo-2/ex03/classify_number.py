def is_positive(number: int) -> bool:
    """receives an integer and returns boolean: True if the number is positive and False otherwise"""
    if number > 0:
        return True
    else:
        return False


#  mypy --strict classify_number.py
