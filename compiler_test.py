"""Module to check the Build folder"""

import os
import subprocess

# -------------------------------------
# check to see if the folder exists
# -------------------------------------
def if_folder(build_path: str) -> bool:

    """The function checks if the folder with builds exists."""

    assert os.path.exists(build_path), 'Folder does not exist.'

# -------------------------------------
# getting a list of subfolders and files
# -------------------------------------
def make_list(build_path: str) -> list:

    """The function accepts a path to the build
    and returns a list of subfolders."""

    folders = next(os.walk(build_path))[1]
    # print(folders)
    return folders

# -------------------------------------
# check to see if the lisf of subfolders and files is empty
# -------------------------------------
def if_empty(folders: list) -> bool:

    """The function checks whether the list is empty."""

    # if folders:
    #    print("the list of folders is not empty")
    assert folders, 'The list of folders is empty.'

# -------------------------------------
# getting the first item of the list of subfolders and files
# -------------------------------------
def show_current_build(folders: list) -> str:

    """The function is to accept a path to an auto-test build
    and returns a first (usually a single one) item of the list."""

    build_number = folders[0]
    # print(build_number)
    return build_number

# -------------------------------------
# getting all the items of the list of subfolders and files
# -------------------------------------
def show_all_the_builds(folders: list) -> list:

    """The function is to accept a path to a build
    and returns all items of the list."""

    build_numbers = folders
    # print(build_numbers)
    return build_numbers
# -------------------------------------------------------------------
# script to build a new version of the manual for the constant value
# -------------------------------------------------------------------
def excecute_script_constant_path(build_number: str) -> bytes:

    """The function is to accept a build number
    as a string to execute a Command Line (CMD) script."""

    out = subprocess.run(
        f"@ECHO OFF&&pushd D:\\pa_config&&set COMLICBITSPATH=D:\\pa_config\\comlicbits.h&&pushd C:\\pa6autotests\\Builds\\{build_number}\\SourceData&&set SOURCEDATA=C:\\pa6autotests\\Builds\\{build_number}\\SourceData&&pushd D:\\gitbash\\help&&D:\\gitbash\\help\\build.cmd", shell=True, check=False)

    return out
