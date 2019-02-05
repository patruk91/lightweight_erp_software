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
    total_column_length = common.sum_values(width_columns) + 1
    # +1 due to end in var:string "|" in print_table
    number_of_columns = len(width_columns)
    width_table = total_column_length + (number_of_columns * PADDINGS)
    return width_table


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your goes code


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    # your code

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
