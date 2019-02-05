""" User Interface (UI) module """


import common


def get_width_columns(table, title_list):
    """
    Find the longest column width in table.
    :param table: database - a text file with data records from different modules
    :return: list with width of columns.
    """
    number_of_columns = len(table[0])
    columns_width_from_file = [max([len(data[indices]) for data in table])
                               for indices in range(number_of_columns)]

    titles_width = (list(len(title) for title in title_list))
    width_columns = [columns_width_from_file[indices] if columns_width_from_file[indices] >
                     titles_width[indices] else titles_width[indices]
                     for indices in range(number_of_columns)]
    return width_columns


def get_position_width_dictionary(table, title_list):
    """
    Create a dictionary with position and column width. Is need to **kwargs
    in print table function. Due to auto-format table.
    :return: Dictionary with position:width
    """
    width_columns = get_width_columns(table, title_list)
    number_of_columns = len(width_columns)
    string_positions = ["pos" + str(indices) for indices in range(number_of_columns)]
    position_value = dict(zip(string_positions, width_columns))
    return position_value


def get_total_width_of_table(table, title_list):
    """
    Calculate total width of table.
    :param table: database - a text file with data records from different modules
    :param title_list: list containing table headers
    :return: int of total sum of each columns and paddings
    """
    PADDINGS = 3
    width_columns = get_width_columns(table, title_list)
    total_column_length = common.add_values(width_columns) + 1
    # +1 due to end in var:string "|" in print_table
    number_of_columns = len(width_columns)
    width_table = total_column_length + (number_of_columns * PADDINGS)
    return width_table


def print_table(table, title_list):
    """
    Prints neatly formatted table with data.
    :param table: database - a text file with data records from different modules
    :param title_list: list containing table headers
    """
    position_width = get_position_width_dictionary(table, title_list)
    width_table = get_total_width_of_table(table, title_list)
    string_pos = ''.join(['| {:^{' + pos + '}} ' for pos in position_width.keys()]) + "|"

    print("-" * width_table)
    print(string_pos.format(*title_list, **position_width))

    print("-" * width_table)
    for record in table:
        print(string_pos.format(*record, **position_width))
        print("-" * width_table)


def print_result(result, label):
    """
    Display results of the special functions.
    :param result: result of the special function e.g string, list or dict
    :param label: label of the result
    """
    print("{} {}\n" .format(label, result))


def print_menu(title, list_options, exit_message):
    """
    Display a menu.
    :param title: menu title
    :param list_options: list of strings - options that will be shown in menu
    :param exit_message: option for back to main menu
    """
    print("{}:" .format(title))
    i = 1
    for option in list_options:
        print("({}) {}" .format(i, option))
        i += 1
    print("(0) {}" .format(exit_message))


def get_inputs(list_labels, title):
    """
    Get list of inputs from the user.
    :param list_labels: labels of inputs
    :param title: title of the "input section"
    :return: list of data given by the user
    """
    if title is not "":
        print("{}" .format(title))
    inputs = []
    for label in list_labels:
        answers = input("{}: " .format(label))
        inputs.append(answers)
    return inputs[0]


def print_error_message(message):
    """
    Displays an error message
    :param message: error message to be displayed
    """
    print("{}" .format(message))
