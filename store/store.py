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
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

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

