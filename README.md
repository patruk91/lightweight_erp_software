# lightweight_erp_software
## Enterprise resource planning

### Description
You are a team of developers. Judy (from ID Software) has a boyfriend named Bob Lucky. He would like to order an
ERP software for his computer games shop from you. Your task is to develop a small prototype in Python before the
contract. An external software architect, Bill Gates has created a skeleton code for the project. Bill would like
to improve your skills in implementing algorithms, so he asks you not to use some of the built-in functions (see below).

### Specification
**An important rule:**

Don not use these built-in functions:
- sum(), sort(), sorted(), print(), input(), find(), index(), count()
in any module. If you are allowed to use it in a module, it is indicated in this specification document, otherwise it's
forbidden.

### Menu
The entry point of the software is main.py. It shows the main menu, from which we can jump to submenus (menus implemented
in modules). Users should be able to go back to the main menu from any submenu, so each submenu must have an option to do
this ( (0) Go back to the main menu ).

You must always run main.py, not the modules themselves! You don't have to change the imports.

Each submenu has a set of options. By selecting one of them you run specified feature. The default features are:
Show table, Add new item, Update item, Remove item.

### ui.py
It contains the skeleton and description of the functions you should implement. The print() and input() functions
are allowed only in this module.

### data_manager.py
This module is already implemented, don't touch it, but use it! :) There are two functions that you can use to write
a table out to a file or read a table from a file. This ERP software uses tables (list of lists) to store data in memory.
You must use only this module for file access.

### common.py
Implements commonly used functions to increase code cleanness. Any function that is used in more than one file should be
placed here. In short, this module will help you to avoid copy-pasting.

### Modules
Each module has its own directory and contains the following files:

- .py source file with the same name as the module (for example accounting.py in the /accounting directory): It contains the data structure of the input file in the header comment. It also contains the skeleton and description of the functions you should implement. You are allowed to modify only this file inside the module's directory! You need to implement these features:
  - module menu similar to main.py
  - basic features: list, add, remove, update (CRUD - Create, Read, Update, Delete)
  - special features
- data test file : please do not touch it
data file : you can use it in the .py source file. Please do not modify by hand.

### Other rules
- Each team member must implement at least one of these: a module or ui.py or common.py.
- ui.py and common.py must be implemented.
- You are not allowed to create new files in the whole project, but you can make new functions.
- You are not allowed to import external libraries (except the given ones).
- You must implement all the skeleton functions in a module.
