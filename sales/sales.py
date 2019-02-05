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


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
