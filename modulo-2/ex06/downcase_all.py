import sys


def downcase_it(string: str) -> str:
    """receives a string and downcases it"""
    return arg.lower()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg_list = sys.argv[1:]
        # Metódo para retirar os args a partir de 0 até o numero indicado - "slice"
        for arg in arg_list:
            print(downcase_it(arg))
    else:
        print("None")

#  mypy --strict downcase_all.py
