""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
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


file_name = "store/games.csv"
table_structure = ["Id", "Title", "Manufacturer", "Price", "In stock"]
options = ("title", "manufacturer", "price", "in stock")


def handle_submenu():
    """Display sub-menu"""
    title = "\nSTORE MODULE"
    list_options = ["Show table", "Add", "Remove", "Update",
                    "Games by manufacturer", "Average number of games by manufacturer"]
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
        get_counts_by_manufacturers(table)
    elif option == "6":
        manufacturer = ui.get_inputs(["Provide a manufacturer"], "")
        get_average_by_manufacturer(table, manufacturer)
    elif option == "0":
        main.main()
    else:
        raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table from store module.
    :param table: database - a text file with data records from store module
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


def get_counts_by_manufacturers(table):
    """
    Calculate how many different kinds of game are available of each manufacturer.
    :param table: database - a text file with data records from inventory module
    :return: dictionary: {[manufacturer]:[count]}
    """
    companies = []
    game = [game_column[1] for game_column in table]
    studio = [company_column[2] for company_column in table]

    for company in table:
        if company[2] not in companies:
            companies.append(company[2])

    games_by_studio = [[game[i] for i in range(len(studio)) if company == studio[i]] for company in companies]
    count_of_games = [len(games) for games in games_by_studio]
    amount_of_games = dict(zip(companies, count_of_games))
    ui.print_result(amount_of_games, "Games amount by manufacturer:")
    return amount_of_games


def get_average_by_manufacturer(table, manufacturer):
    """
    Average amount of games in stock of a given manufacturer
    :param table: database - a text file with data records from inventory module
    :param manufacturer: name of company
    :return: average number
    """
    ui.print_table(table, table_structure)
    studio_and_stock = [(record[2], record[4]) for record in table if record[2] == manufacturer]
    amount_in_stock = [int(games[1]) for games in
                       studio_and_stock if games[0] == manufacturer]
    avg_count = [common.add_values(amount_in_stock) / len(amount_in_stock)][0]
    ui.print_result(avg_count, "Average amount of games in stock of a given manufacturer:")
    return avg_count

