""" Common module
implement commonly used functions here
"""


import random


types_list = ("month", "day", "year", "amount", "subscribed", "birth year", "purchase year", "durability", "price", "in stock")
border_conditions = (12, 31, 3000, 1000000, 1, 2019, 2019, 10000000, 1000000, 1000000)


def generate_random(table):
    """
    Generates random and unique string.
    :param table: database - a text file with data records from different modules
    :return: Random unique id/key
    """
    unique_values = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                     "1234567890", "\`~!@#$%^&*()_-+={[}}|:,'<>?/"]
    while True:
        string_generator = [random.choice(char) for char in unique_values for _ in range(2)]
        random.shuffle(string_generator)
        generated = "".join(string_generator)
        id_list = [column_id_key[0] for column_id_key in table]
        if generated not in id_list:
            return generated


def add_values(numbers_list):
    """
    add values from list.
    :param numbers_list: list with integers.
    :return: add(data_list)
    """
    add_numbers = 0
    for number in numbers_list:
        add_numbers += number
    return add_numbers


def handle_sort_names(longest_names):
    """
    Sort the string data in ascending order.
    :param longest_names: Name of people to sort.
    :return: list with sorted names
    """
    x = 0
    while x < len(longest_names):
        for indice in range(len(longest_names) - 1):
            if longest_names[indice] > longest_names[indice + 1]:
                temp = longest_names[indice + 1]
                longest_names[indice + 1] = longest_names[indice]
                longest_names[indice] = temp
        x += 1
    return longest_names


def get_indices(user_input, user_option):
    """
    Find index in list
    :param user_input: value provided from user
    :param user_option: list with available user parameters
    :return: i - index
    """
    for i in range(len(user_option)):
        if user_input == user_option[i]:
            return i


def check_is_number(user_input):
    """
    Check if input parameter is number.
    :param user_input: value provided from user
    :return: boolean
    """
    if user_input.isdigit() and int(user_input) >= 0:
        return True
    return False


def data_types_dependent_on_numbers(type_of_data):
    """
    Check if data type is dependent on numbers.
    :param type_of_data:
    :return: boolean
    """
    if type_of_data in types_list:
        return True
    return False


def check_data_in_range(user_input, user_option):
    """
    Check if data is in certain boundaries
    :param user_input: value provided from user
    :param user_option: list with available user parameters
    :return: boolean
    """
    indice = get_indices(user_option, types_list)

    if user_option == "subscribed":
        if int(user_input) == 0 or border_conditions[indice] == int(user_input):
            return True
    else:
        if border_conditions[indice] >= int(user_input) > 0:
            return True
    return False
