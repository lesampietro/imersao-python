def format_names(dictionary: dict[str, str]) -> list[str]:
    """Receives a dictionary and returns a list of Name + Surname, with the first letter capitalized"""
    dict_list = [f"{key.capitalize()} {value.capitalize()}" for key, value in dictionary.items()]
    return dict_list

# dictionary = {"jean": "valjean", "grace": "hopper", "xavier": "niel", "fifi": "brindacier"}

# print(format_names(dictionary))

# ----------------------------------------------------------
# Other possible solutions
# dict_list = list(map(lambda x: f"{x[0].capitalize()} {x[1].capitalize()}", dictionary.items()))

# dict_list = []
# for key, value in dictionary.items():
#     key_cap = key.capitalize()
#     value_cap = value.capitalize()
#     dict_list.append(f'{key_cap} {value_cap}')
