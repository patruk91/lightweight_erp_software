""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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


file_name = "crm/customers.csv"
table_structure = ["Id", "Name", "Email", "Subscribed"]


def handle_submenu():
    """Display sub-menu"""
    title = "\nCRM MODULE"
    list_options = ["Show table", "Add", "Remove", "Update",
                    "Show id of customer with longest name", "Show customers are subscribed newsletter"]
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
        get_longest_name_id(table)
    elif option == "6":
        get_subscribed_emails(table)
    elif option == "0":
        main.main()
    else:
        raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table from store module.
    :param table: database - a text file with data records from crm module
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

def get_longest_name_id(table):
    """
    Find id of the customer with the longest name.
    :param table: list of lists with data form crm department
    :return: Id of the longest name (if there are more than one, return
             the last by alphabetical order of the names)
    """
    names = [name_column[1] for name_column in table]
    names_length = [len(name_column[1]) for name_column in table]
    max_len_name = max(names_length)
    longest_names = [names[i] for i in range(len(names)) if names_length[i] == max_len_name]

    longest_names = common.handle_sort_names(longest_names)
    get_indice_name = [indice for indice in range(len(names)) if names[indice] == longest_names[-1]][0]
    name_id = table[get_indice_name][0]
    ui.print_result(name_id, "Id of the customer with longest name:")
    return name_id


def get_subscribed_emails(table):
    """
    Find customers has subscribed the newsletter.
    :param table: list of lists with data form crm department
    :return: list with subscribed customers
    """
    subscribed_emails = [record[2] + ";" + record[1] for record in table if int(record[3]) == 1]
    # record[1] == name, record[2] == email, record[3] == subscribed or not
    ui.print_result(subscribed_emails, "Customers that subscribed emails:")
    return subscribed_emails
