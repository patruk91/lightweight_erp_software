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
options = ("name", "email", "subscribed")


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
    :param table: text file where are included some information.
    :param id_: id of a record to update
    :return: list of list with updated record
    """
    searched_record = common.get_correct_id(table, id_, table_structure)
    while True:
        user_input = ui.get_inputs(["What do you want change?"], "")
        indice_option = common.get_indices(user_input, options)
        if user_input in options:
            new_record = common.check_possibility_update_record(user_input, searched_record, indice_option)
            if new_record != None:
                break
        else:
            ui.print_error_message("Please provide a correct record to edit!".upper())

    data_manager.write_table_to_file(file_name, table)
    ui.print_table([searched_record], table_structure)
    return table


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
