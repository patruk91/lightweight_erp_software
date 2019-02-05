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


def handle_submenu():
    """Display sub-menu"""
    title = "\nSALES MODULE"
    list_options = ["Show table", "Add", "Remove", "Update",
                    "Show id of item with lowest selling price", "Show items sold between dates"]
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
        get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
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
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

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
    title_with_min_price = [record[1] for record in table if int(record[2]) == price]
    # record[1] == title_column, record[2] == price_column
    sorted_title = common.handle_sort_names(title_with_min_price)

    result = [record for record in table if record[1] == sorted_title[-1]][0]
    ui.print_result(result[0], "Id of item with lowest price:")
    return result[0]


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Calcualte items, which are sold between two given dates.
    :param table: text file where are included some information.
    :param ..._from: choose "MM/YY/DD" from start to search
    :param ..._to: choose "MM/YY/DD" to start to search
    :return: list of lists with items in range.
    """

    date_from = "".join(str(year_from) + str(month_from) + str(day_from))
    date_to = "".join(str(year_to) + str(month_to) + str(day_to))
    dates_to_check = ["".join(str(record[5]) + str(record[3]) + str(record[4])) for record in table]
    # convert to YEAR/MONTH/DAY

    items_sold_between = [table[i] for i in range(len(table)) if date_from < dates_to_check[i] < date_to]
    convert_items = [[int(number) if number.isdigit() else number
                      for number in record] for record in items_sold_between]
    ui.print_result(convert_items, "Items from range:")
    return convert_items
