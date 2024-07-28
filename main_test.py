"""The main module of the compiler."""

import os
import subprocess

constants = {
    "BUILD": "C:\\pa6autotests\\Builds\\30582",
    "HEADER": "D:\\pa_config",
    "SCRIPT": "D:\\gitbash\\help"
}

# TODO: проверить, что каждый путь валиден
# TODO: получить список файлов для каждого пути
# TODO: проверить, что нужный файл лежит по данному пути по каждому пути
# TODO: запустить скрипт

# -------------------------------------
# check to see if the folder exists
# -------------------------------------
def if_folder(const: dict) -> bool:

    """The function checks if the folder with the PA build exists."""

    for folder in constants["BUILD"]:
        assert os.path.exists(folder), 'Folder does not exist.'

# -------------------------------------------------------------------
# script to build a new version of the manual for the constant value
# -------------------------------------------------------------------
def excecute_script_constant_path(build: str, script: str, header: str) -> bytes:

    """The function is to accept a build number
    as a string to execute a Command Line (CMD) script."""

    # from where does it start?

    out = subprocess.run(
        f"@ECHO OFF&&pushd D:\\pa_config&&set COMLICBITSPATH={header}&&pushd {build}\\SourceData&&set SOURCEDATA={build}\\SourceData&&pushd D:\\gitbash\\help&&D:\\gitbash\\help\\build.cmd", shell=True, check=False)

    return out


    # out = subprocess.run(
    #     f"@ECHO OFF&&
    #     set COMLICBITSPATH={header}&&
    #     set SOURCEDATA={build}&&
    #     pushd D:\\gitbash\\help&&D:\\gitbash\\help\\build.cmd", 
    #     shell=True, 
    #     check=False
    #     )

if_folder(constants)
