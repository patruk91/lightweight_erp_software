""" Common module
implement commonly used functions here
"""


import random
import ui

types_list = (
    "month",
    "day",
    "year",
    "amount",
    "subscribed",
    "birth year",
    "purchase year",
    "durability",
    "price",
    "in stock")

border_conditions = (
    12,
    31,
    3000,
    1000000,
    1,
    2019,
    2019,
    10000000,
    1000000,
    1000000)


def generate_random(table):
    """
    Generates random and unique string.
    :param table: database - a text file with data records from different modules
    :return: Random unique id/key
    """
    unique_values = [
        "abcdefghijklmnopqrstuvwxyz",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "1234567890",
        "\`~!@#$%^&*()_-+={[}}|:,'<>?/"]
    while True:
        string_generator = [random.choice(char)
                            for char in unique_values for _ in range(2)]
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
        if int(user_input) == 0 or border_conditions[indice] == int(
                user_input):
            return True
    else:
        if border_conditions[indice] >= int(user_input) > 0:
            return True
    return False


def get_correct_id(table, id_, table_structure):
    """
    Check if user provided id which is in database(table)
    :param table: text file where are included some information.
    :param id_: id/key record to be find
    :return: record which is compatible with id
    """
    while True:
        searched_record = [record for record in table if id_ == record[0]]
        if searched_record != []:
            break
        ui.print_error_message("Please provide correct id!".upper())
        id_ = ui.get_inputs(["Enter id of record who you want edit"], "")

    ui.print_table(searched_record, table_structure)
    searched_record = searched_record[0]  # unpack from list of lists
    return searched_record


def check_possibility_update_record(
        user_input,
        searched_record,
        indice_option):
    """
    Check if is possible to update record in table.
    :param user_input: parameter to change by user in each module
    :param searched_record: id of record, which user want to change
    :param indice_option: index of this parameter in each module
    :return: updated record with new value
    """
    if data_types_dependent_on_numbers(user_input):
        number_to_check = ui.get_inputs(["Please provide a new value"], "")
        if check_is_number(number_to_check) and check_data_in_range(
                number_to_check, user_input):
            searched_record[indice_option + 1] = number_to_check
            return searched_record
        else:
            ui.print_error_message("Please provide a correct value!".upper())
    else:
        searched_record[indice_option] = user_input
        return searched_record
