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


def sum_values(numbers_list):
    """
    Sum values from list.
    :param numbers_list: list with integers.
    :return: sum(data_list)
    """
    sum_numbers = 0
    for number in numbers_list:
        sum_numbers += number
    return sum_numbers
