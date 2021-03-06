""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
# main module
import main


file_name = "sales/sales.csv"
table_structure = ["Id", "Title", "Price", "Month", "Day", "Year"]
options = ("title", "price", "month", "day", "year")


def handle_submenu():
    """Display sub-menu"""
    title = "\nSALES MODULE"
    list_options = [
        "Show table",
        "Add",
        "Remove",
        "Update",
        "Show id of item with lowest selling price",
        "Show items sold between dates"]
    exit_message = "Back to main menu"
    ui.print_menu(title, list_options, exit_message)


def start_module():
    """
    Display menu and wait for user choice.
    """
    handle_submenu()
    table = data_manager.get_table_from_file(file_name)

    inputs = ui.get_inputs(["Please choose your option"], " ")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        ui.print_table(table, table_structure)
        id_ = ui.get_inputs(["Enter id of record to delete"], "")
        remove(table, id_)
    elif option == "4":
        ui.print_table(table, table_structure)
        id_ = ui.get_inputs(["Enter id of record which you want to edit"], "")
        update(table, id_)
    elif option == "5":
        get_lowest_price_item_id(table)
    elif option == "6":
        date_options = handle_user_dates()
        get_items_sold_between(
            table,
            date_options[0],
            date_options[1],
            date_options[2],
            date_options[3],
            date_options[4],
            date_options[5])
    elif option == "0":
        main.main()
    else:
        raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table from store module.
    :param table: database - a text file with data records from sales module
    """
    ui.print_table(table, table_structure)


def add(table):
    """
    Ask user for inputs and update the table.
    :param table: database - a text file with data records from accounting module
    :return: updated table with new record
    """
    show_table(table)
    new_record = []
    new_record.append(common.generate_random(table))

    i = 0
    while i < len(options):
        user_input = ui.get_inputs(["Enter {}" .format(options[i])], "")
        if common.data_types_dependent_on_numbers(options[i]):
            if common.check_is_number(user_input) and common.check_data_in_range(
                    user_input, options[i]):
                new_record.append(user_input)
                i += 1
            else:
                ui.print_error_message(
                    "Please provide a correct value!".upper())
        else:
            new_record.append(user_input)
            i += 1

    updated_table = table + [new_record]
    data_manager.write_table_to_file(file_name, updated_table)
    show_table(updated_table)

    return updated_table


def remove(table, id_):
    """
    Remove a record with a given id from the table.
    :param table: text file where are included some information.
    :param id_: id/key record to be removed
    :return: list without specified record.
    """
    update_table = [records for records in table if id_ not in records]
    data_manager.write_table_to_file(file_name, update_table)
    show_table(update_table)
    return update_table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.
    :param table: text file where are included some information.
    :param id_: id of a record to update
    :return: list of list with updated record
    """
    searched_record = common.get_correct_id(table, id_, table_structure)
    while True:
        user_input = ui.get_inputs(["What do you want change?"], "")
        indice_option = common.get_indices(user_input, options)
        if user_input in options:
            new_record = common.check_possibility_update_record(
                user_input, searched_record, indice_option)
            if new_record is not None:
                break
        else:
            ui.print_error_message(
                "Please provide a correct record to edit!".upper())

    data_manager.write_table_to_file(file_name, table)
    ui.print_table([searched_record], table_structure)
    return table


def get_lowest_price_item_id(table):
    """
    Find item, which was sold for the lowest price. If there are more than
    one item at the lowest price, return the last item by alphabetical
    order of the title
    :param table: text file where are included some information.
    :return: id of item
    """
    price = min([int(price_column[2]) for price_column in table])
    title_with_min_price = [record[1]
                            for record in table if int(record[2]) == price]
    # record[1] == title_column, record[2] == price_column
    sorted_title = common.handle_sort_names(title_with_min_price)

    result = [record for record in table if record[1] == sorted_title[-1]][0]
    ui.print_result(result[0], "Id of item with lowest price:")
    return result[0]


def handle_user_dates():
    """
    Ask user for month, year, day from and to search.
    :return: list with dates: from, to
    """
    questions = ["Enter month from do you want search", "Enter day from do you want search",
                 "Enter year from do you want search", "Enter month do you want look for",
                 "Enter day do you want look for", "Enter year do you want look for"]
    dates = ["month", "day", "year", "month", "day", "year"]
    options = []
    i = 0
    while i < len(questions):
        value = ui.get_inputs([questions[i]], "")
        if common.check_is_number(value):
            if common.check_data_in_range(value, dates[i]):
                options.append(int(value))
                i += 1
    return options


def get_items_sold_between(
        table,
        month_from,
        day_from,
        year_from,
        month_to,
        day_to,
        year_to):
    """
    Calcualte items, which are sold between two given dates.
    :param table: text file where are included some information.
    :param ..._from: choose "MM/YY/DD" from start to search
    :param ..._to: choose "MM/YY/DD" to start to search
    :return: list of lists with items in range.
    """
    date_from = "".join(str(year_from) + str(month_from) + str(day_from))
    date_to = "".join(str(year_to) + str(month_to) + str(day_to))
    dates_to_check = ["".join(str(record[5]) +
                              str(record[3]) +
                              str(record[4])) for record in table]
    # convert to YEAR/MONTH/DAY

    items_sold_between = [table[i] for i in range(
        len(table)) if date_from < dates_to_check[i] < date_to]
    convert_items = [[int(number) if number.isdigit() else number
                      for number in record] for record in items_sold_between]
    ui.print_result(convert_items, "Items from range:")
    show_table(items_sold_between)
    return convert_items
