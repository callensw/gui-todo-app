import os

# Get the directory of the current script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Construct the absolute path to todos.txt
FILEPATH = os.path.join(SCRIPT_DIR, r"todos.txt")


def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of
    to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
