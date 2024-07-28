"""Module to compile a new version of the Help when the path is a constant variable"""

import os

BUILD_PATH = "C:/pa6autotests/Builds"

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
# get a list of the subfolders
# -------------------------------------
def if_all_empty(folders: list) -> list:

    """The function checks whether the build folders are empty."""

    builds = []
    for folder in folders:
        folder = BUILD_PATH + f"/{folder}"
        # print(folder)
        if os.listdir(folder):
            # print(folder)
            # assert folder, "The folder is empty."
            # print('The folder is not empty.')

            builds.append(folder)
    
    print(builds)
    return builds

# -------------------------------------
# accepting a list of non-empty builds to pass them to the script
# -------------------------------------
def choose_build(builds: list) -> str:

    """The function accepts a list of non-empty folders and
    stores one value to pass it to the script."""

    for build in builds:
        print("The list of build is as follows:")
        print(build)
        print("Choose a build to compile the User's Manual.")

    stored = input()
    print("Entered value: " + f"{stored}")
    return stored


if_all_empty(make_list(BUILD_PATH))
