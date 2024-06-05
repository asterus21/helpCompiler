"""Module to compile a new version of the Help"""

import os
import subprocess
from icecream import ic

BUILD_PATH = "C:/pa6autotests/Builds"

# check to see if the folder exists
def if_folder(build_path: str) -> bool:

    """The function checks if the folder with builds exists."""

    if os.path.exists(build_path):
        ic('pass')
    else:
        raise ValueError('The folder does not exist.')

# getting a list of subfolders and files
def make_list(build_path: str) -> list:

    """The function accepts a path to the build
    and returns a list of subfolders."""

    list_folders = os.listdir(build_path)
    return list_folders

# check to see if the lisf of subfolders and files is empty
def if_empty(list_folders: list) -> bool:

    """The function checks whether the list is empty."""

    if list_folders:
        ic('pass')
    else:
        raise ValueError('The folder is empty.')

# getting the first item of the list of subfolders and files
def show_current_build(list_folders: list) -> str:

    """The function is to accept a path to an auto-test build
    and returns a first (usually a single item) of the list."""

    build_number = list_folders[0]
    ic(build_number)
    return build_number

# script to build a new version of the manual
def excecute_script(build_number: str) -> bytes:

    """The function is to accept a build number
    as a string to execute a Command Line (CMD) script."""

    out = subprocess.run(
        f"@ECHO OFF&&pushd D:\\pa_config&&set COMLICBITSPATH=D:\\pa_config\\comlicbits.h&&pushd C:\\pa6autotests\\Builds\\{build_number}\\SourceData&&set SOURCEDATA=C:\\pa6autotests\\Builds\\{build_number}\\SourceData&&pushd D:\\gitbash\\help&&D:\\gitbash\\help\\build.cmd", shell=True, check=False)

    return out
