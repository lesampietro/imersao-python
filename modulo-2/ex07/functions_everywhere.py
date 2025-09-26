import sys


def shrink(string: str) -> str:
    """receives a string and returns only its first eight characters"""
    return string[:8]


# slices method = string[start:stop]


def enlarge(string: str) -> str:
    """receives a string and adds "Z" to the end of the word till it reaches eight characters, and then returns the new string"""
    arg_len = len(string)
    string = string + ("Z" * (8 - arg_len))
    return string


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg_list = sys.argv[1:]
        for arg in arg_list:
            arg_len = len(arg)
            if arg_len > 8:
                print(shrink(arg))
            elif arg_len < 8:
                print(enlarge(arg))
            else:
                print(arg)
    else:
        print("None")

#  mypy --strict functions_everywhere.py
