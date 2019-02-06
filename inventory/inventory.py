""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
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


file_name = "inventory/inventory.csv"
table_structure = ["Id", "Name", "Manufacturer", "Purchase Year", "Durability"]
actual_year = 2017
options = ("name", "manufacturer", "purchase year", "durability")



def handle_submenu():
    """Display sub-menu"""
    title = "\nINVENTORY MODULE"
    list_options = ["Show table", "Add", "Remove", "Update",
                    "Show articles that aren't exceeded durability", "Average durability for each manufacturer"]
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
        get_available_items(table)
    elif option == "6":
        get_average_durability_by_manufacturers(table)
    elif option == "0":
        main.main()
    else:
        raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table from store module.
    :param table: database - a text file with data records from inventory module
    """
    ui.print_table(table, table_structure)


def add(table):
    """
    Ask user for inputs and update the table.
    :param table: database - a text file with data records from accounting module
    :return: updated table with new record
    """
    new_record = []
    new_record.append(common.generate_random(table))

    i = 0
    while i < len(options):
        user_input = ui.get_inputs(["Enter {}" .format(options[i])], "")
        if common.data_types_dependent_on_numbers(options[i]):
            if common.check_is_number(user_input) and common.check_data_in_range(user_input, options[i]):
                new_record.append(user_input)
                i += 1
            else:
                ui.print_error_message("Please provide a correct value!".upper())
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

def get_available_items(table):
    """
    Find items with actual durability
    :param table: database - a text file with data records from inventory module
    :return: list of items with actual durability
    """
    actual_durability = [record for record in table if
                         int(record[3]) + int(record[4]) >= actual_year]
    # record[3] == year, record[4] == durability
    convert_actual_dur = [[int(number) if number.isdigit() else number
                           for number in record] for record in actual_durability]
    ui.print_result(convert_actual_dur, "List of items with actual durability:")
    return convert_actual_dur


def get_average_durability_by_manufacturers(table):
    """
    Calculate average durability by manufacturers
    :param table: database - a text file with data records from inventory module
    :return: dictionary with average of durability
    """
    list_of_manufacturer = []
    companies_durability = [(record[2], record[4]) for record in table]
    # record[2] == company name, durability

    for records in table:
        if records[2] not in list_of_manufacturer:
            list_of_manufacturer.append(records[2])
            # manufacturers needs to be in order

    list_of_durability = [[int(column_company[1]) for column_company in
                           companies_durability if company == column_company[0]]
                          for company in list_of_manufacturer]

    average_durability = [str(common.add_values(number_list) / len(number_list))
                          for number_list in list_of_durability]

    convert_avg_dur = [int(float(num)) if ".0" in num else float(num)
                       for num in average_durability]

    dict_avg_dur = dict(zip(list_of_manufacturer, convert_avg_dur))
    ui.print_result(dict_avg_dur, "Average durability by manufacturer:")
    return dict_avg_dur
