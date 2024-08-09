"""Main module"""

import subprocess
import paths

FILE_PATH = "C:\\variables.txt"
# the list is considered to be on the 'C:' volume and have the '.txt' format

paths.if_file(FILE_PATH)

file = paths.file_open(FILE_PATH)

paths.if_folder(file)

lists = paths.list_of_files(file)

paths.if_header(lists)
paths.if_script(lists)

buil = file[0]
conf = file[1]
scrp = file[2]

def excecute_script_constant_path(bld: str, cnf: str, spt: str) -> bytes:

    """The function is to accept a build number
    as a string to execute a Command Line (CMD) script."""

    out = subprocess.run(f"@ECHO OFF&&pushd {cnf}&&set COMLICBITSPATH={cnf}\\comlicbits.h&&pushd {bld}\\SourceData&&set SOURCEDATA={bld}\\SourceData&&pushd {spt}&&{spt}\\build.cmd", shell=True, check=False)

    return out

if __name__ == "__main__":
    excecute_script_constant_path(buil, conf, scrp)
