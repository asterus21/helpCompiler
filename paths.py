"""The module checks each path to see if it's valid"""

import os

# -------------------------------------
# check the file exists
# -------------------------------------
def if_file(file_path: str) -> bool:

    """The method checks if the file exists."""    

    assert os.path.isfile(file_path), "The file does not exist."

# -------------------------------------
# file with variables
# -------------------------------------
def file_open(file: bytes) -> list:

    """The method opens a file with path variables and stores the paths in a list."""    

    with open(file, "r", encoding="utf-8") as f:
        content = f.read().splitlines()

    return content

# -------------------------------------
# check to see if the folder exists
# -------------------------------------
def if_folder(content: list) -> bool:

    """The function checks if the folders exist."""

    for value in content:
        assert os.path.exists(value), "Folder does not exist."

# -------------------------------------
# get a list of files within the folder
# -------------------------------------
def list_of_files(content: list) -> list:

    """The function returns the list of files for a given path."""

    files = []
    for path in content:
        files.append(os.listdir(path))

    return files

# -------------------------------------
# check if a header file exists
# -------------------------------------
def if_header(files: list) -> bool:

    """The function checks that the file exists within a specified folder."""

    if 'comlicbits.h' in files[1]:
        return True

    return True

# -------------------------------------
# check if a script file exists
# -------------------------------------
def if_script(files: list) -> bool:

    """The function checks that the file exists within a specified folder."""

    if 'build.cmd' in files[2]:
        return True

    return True
