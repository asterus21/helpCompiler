"""Main module"""

import subprocess
import paths

FILE_PATH = "C:\\variables.txt"

buil = paths.file_open(FILE_PATH)[0]
conf = paths.file_open(FILE_PATH)[1]
scrp = paths.file_open(FILE_PATH)[2]

# the list is considered to be on the 'C:' volume and have the '.txt' format

def excecute_script_constant_path(bld: str, cnf: str, spt: str) -> bytes:

    """The function is to accept a build number
    as a string to execute a Command Line (CMD) script."""

    out = subprocess.run(f"@ECHO OFF&&pushd {cnf}&&set COMLICBITSPATH={cnf}\\comlicbits.h&&pushd {bld}\\SourceData&&set SOURCEDATA={bld}\\SourceData&&pushd {spt}&&{spt}\\build.cmd", shell=True, check=False)

    return out

if __name__ == "__main__":
    excecute_script_constant_path(buil, conf, scrp)
