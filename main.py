"""The module starts the script to build a new version of the User's Manual"""

import subprocess
import paths

build_path = paths.file_open(paths.FILE_PATH)[0]
build_header = paths.file_open(paths.FILE_PATH)[1]
build_script = paths.file_open(paths.FILE_PATH)[2]

# print(
#     build_path,
#     build_header,
#     build_script
# )

# -------------------------------------------------------------------
# script to build a new version of the manual for the constant values
# -------------------------------------------------------------------
def excecute_script_constant_path(build_path: str) -> bytes:

    """The function is to accept a build number
    as a string to execute a Command Line (CMD) script."""


    out = subprocess.run(f"@ECHO OFF&&pushd D:\\pa_config&&set COMLICBITSPATH=D:\\pa_config\\comlicbits.h&&pushd C:\\pa6autotests\\Builds\\{build_path}\\SourceData&&set SOURCEDATA=C:\\pa6autotests\\Builds\\{build_path}\\SourceData&&pushd D:\\gitbash\\help&&D:\\gitbash\\help\\build.cmd", shell=True, check=False)

    return out
