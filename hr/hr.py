""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
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


file_name = "hr/persons.csv"
table_structure = ["Id", "Name", "Birth Year"]
options = ("name", "birth year")


def handle_submenu():
    """Display sub-menu"""
    title = "\nHR MODULE"
    list_options = ["Show table", "Add", "Remove", "Update",
                    "Oldest person", "Closest person to average age"]
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
        get_oldest_person(table)
    elif option == "6":
        get_persons_closest_to_average(table)
    elif option == "0":
        main.main()
    else:
        raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table from store module.
    :param table: database - a text file with data records from hr module
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

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


def get_oldest_person(table):
    """
    Find the oldest persons
    :param table: database - a text file with data records from hr module
    :return: list with oldest persons name
    """
    oldest_year = min([year_column[2] for year_column in table])
    oldest_names = [record[1] for record in table if record[2] == oldest_year]
    # record[1] == name, record[2] == year
    ui.print_result(oldest_names, "Oldest persons:")
    return oldest_names


def get_persons_closest_to_average(table):
    """
    Find the person, which is closest to average age
    :param table: list of lists with data form hr department
    :return: list with persons, which is closet to average age
    """
    years = [int(year_column[2]) for year_column in table]
    years_avg = common.add_values(years) / len(years)
    similar_years = min(years, key=lambda x: abs(x - years_avg))

    closest_person = [record[1] for record in table if int(record[2]) == similar_years]
    # record[1] == name, record[2] == year
    ui.print_result(closest_person, "Closest person to average year:")
    return closest_person
