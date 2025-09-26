import sys


def square_even_numbers(int_list: list[int]) -> list[int]:
    """receives a list and checks if there are even numbers. if so, it returns a new list with all squared evens"""
    return [number**2 for number in int_list if number % 2 == 0]


# list comprehension = [<expression> for <item> in <iterable> if <condition>]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg_list = sys.argv[1:]
        for arg in arg_list:
            split_arg = arg.split()
            int_list = list(map(int, split_arg))
            res_list = square_even_numbers(int_list)
            print(f"Squared evens: {res_list}")
    else:
        print("None")

# map() applies a function to each item of an iterable (e.g> a list)
# map is an iterator, so it needs to be converted into a list> list(map(int, split_arg))

#  mypy --strict transform.py
