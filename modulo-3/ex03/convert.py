import sys


def convert(num: str) -> None:
    """Receives an argument from the command line (type: str) and converts it to a float. Conversion errors are treated with Exceptions"""
    try:
        print(float(num))
        # conversao de int para float
    except ValueError:
        print("conversion impossible")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        convert(sys.argv[1])
    else:
        print("no arguments passed")
