""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
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


file_name = "accounting/items.csv"
table_structure = ["Id", "Month", "Day", "Year", "Type", "Amount"]
options = ("month", "day", "year", "type", "amount")


def handle_submenu():
    """Display sub-menu"""
    title = "\nACCOUNTING MODULE"
    list_options = ["Show table", "Add", "Remove", "Update",
                    "Show year with highest profit", "Average profit in given year"]
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
        which_year_max(table)
    elif option == "6":
        year = ui.get_inputs(["Provide year"], "")
        avg_amount(table, year)
    elif option == "0":
        main.main()
    else:
        raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table from store module.
    :param table: database - a text file with data records from accounting module
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

def which_year_max(table):
    """
    Find the year where was highest income.
    :param table: database - a text file with data records from accounting module
    :return: year with highest income
    """
    transaction_type = [column_type[4] for column_type in table]
    amount = [int(column_amount[5]) for column_amount in table]
    max_amount = max([int(amount[5]) for amount in table if amount[4] == "in"])
    year_indices = [indices for indices in range(len(amount))
                    if amount[indices] == max_amount and
                    transaction_type[indices] == "in"]

    if len(year_indices) > 1:
        years_max = [int(table[year_indices[indices]][3]) for indices in range(len(year_indices))]
        return years_max

    year_indices = year_indices[0]
    year_max = table[year_indices][3]
    ui.print_result(year_max, "Highest profit was in:")
    return int(year_max)


def avg_amount(table, year):
    """
    Calculate average (per item) profit in a given year.
    :param table: database - a text file with data records from accounting module
    :param year: year to search
    :return: profit = (income - outflow)/(items count)
    """
    cash_flow = [(record[4], int(record[5])) for record in table if int(record[3]) == int(year)]
    income = [wages[1] for wages in cash_flow if wages[0] == "in"]
    outflow = [wages[1] for wages in cash_flow if wages[0] == "out"]
    profit = (common.add_values(income) - common.add_values(outflow)) / len(cash_flow)
    ui.print_result(profit, "Average profit in was:")
    return profit
