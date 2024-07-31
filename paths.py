"""The module checks each path to see if it's valid"""

import os

KEYS = ["BUILD", "HEADER", "SCRIPT"]
FILE_PATH = "C:\\variables.txt"
# the second list where paths are stored is considered to be at 'C:' and have the .txt format

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

    # print(content)
    return content

# -------------------------------------
# turn a list into a dictionary
# -------------------------------------
def list_to_dict(content: list) -> dict:

    """The function turn a list into a dictionary"""

    dict_ = dict(zip(KEYS, content))
    # print(dict_)
    return dict_

# -------------------------------------
# check to see if the folder exists
# -------------------------------------
def if_folder(dict_: dict) -> bool:

    """The function checks if the folder with the PA build exists."""

    for value in dict_.values():
        # print(value)
        assert os.path.exists(value), "Folder does not exist."

# -------------------------------------
# get a list of folders
# -------------------------------------
def get_paths(dict_: dict) -> list:

    """The function returns a list of paths."""

    paths = []
    for value in dict_.values():
        paths.append(value)

    # print(paths[0])
    return paths

# -------------------------------------
# get a list of files within the folder
# -------------------------------------
def list_of_files(paths: list) -> list:

    """The function returns the list of files for a given path."""

    files = []
    for path in paths:
        files.append(os.listdir(path))

    # print(files)
    return files

# -------------------------------------
# check if a header file exists
# -------------------------------------
def if_header(files: list) -> None:

    """The function checks that the file exists within a specified folder."""

    if 'comlicbits.h' in files[1]:
        print("'comlicbits.h' has been found")
        return True

    return None

# -------------------------------------
# check if a script file exists
# -------------------------------------
def if_script(files: list) -> None:

    """The function checks that the file exists within a specified folder."""

    if 'build.cmd' in files[2]:
        print("'build.cmd' has been found")
        return True

    return None
