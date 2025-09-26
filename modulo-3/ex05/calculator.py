from typing import Any
import sys


def add(num1: int, num2: int) -> int:
    """Calculates sum of two integers passed as arguments from command line"""
    return num1 + num2


def subtract(num1: int, num2: int) -> int:
    """Subtracts the second parameter from the first one, both passed as arguments from command line"""
    return num1 - num2


def multiply(num1: int, num2: int) -> int:
    """Multiplies two integers passed as arguments from command line"""
    return num1 * num2


def divide(num1: int, num2: int) -> float:
    """Receives two number as arguments from the command line and divides num1 by num2. Division by zero error is treated with Exception"""
    divide_by_zero(num2)
    result = num1 / num2
    return result


def divide_by_zero(num2: int) -> None:
    if num2 == 0:
        raise ValueError("Cannot divide by zero")


def power(base: int, exponent: int) -> Any:
    """Calculates base raised to the power of exponent"""
    return base ** exponent


if __name__ == "__main__":
    if len(sys.argv) > 2:
        num1, num2 = int(sys.argv[1]), int(sys.argv[2])
        print(f"Add operation: {add(num1, num2)}")
        print(f"Subtract operation: {subtract(num1, num2)}")
        print(f"Multiply operation: {multiply(num1, num2)}")

        try:
            print(f"Divide operation: {divide(num1, num2)}")
        except ValueError as e:
            print(f"Divide operation: Error - {e}")

        print(f"Power operation: {power(num1, num2)}")

    else:
        nl = '\n'
        print(f"Error: arguments missing.{nl}Usage example: python3 calculator.py <arg1> <arg2>")
