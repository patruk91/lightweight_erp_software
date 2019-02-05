""" Common module
implement commonly used functions here
"""


import random


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
