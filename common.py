""" Common module
implement commonly used functions here
"""

import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''

    # your code

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
