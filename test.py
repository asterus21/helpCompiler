# -------------------------------------
# starting a script from a specified path
# -------------------------------------

import os

print("Enter the absolute path to the build:")
stdin = input()

def current_folder(stdin: str) -> str:

    """The function accepts path to a build."""

    assert os.path.exists(stdin), "The folder does not exist, please enter the correct path."
    # print(stdin)
    return stdin

#current_folder(stdin)

# -------------------------------------
# check to see if the subfolders are empty
# -------------------------------------
def if_all_empty(build_numbers: list) -> bool:

    """The function checks whether the build folders are empty."""

    for folder in build_numbers:
        folder = "C:/pa6autotests/Builds" + f"/{folder}"
        # print(folder)
        if os.listdir(folder):
            # print(folder)
            # assert folder, "The folder is empty."
            # print('The folder is not empty.')

            return folder
