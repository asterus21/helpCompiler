import os
import subprocess


class HelpCompiler:

    """Class to include functions to compile
    the current version of the User Manual."""

    def __init__(self) -> None:
        pass

    def show_current_build(self, build_path: str) -> str:

        """The function is to accept a path to an auto-test build
        and returns a first (usually a single item) of the list."""

        build_number = os.listdir(path=build_path)[0]
        
        return build_number

    def excecute_script(self, build_number: str) -> bytes:

        """The function is to accept a build number
        as a string to execute a Command Line (CMD) script."""

        out = subprocess.run(
            "@ECHO OFF && pushd D:\\pa_config && set COMLICBITSPATH=D:\\pa_config\\comlicbits.h && pushd C:\\pa6autotests\\Builds\\%s\\SourceData && set SOURCEDATA=C:\\pa6autotests\\Builds\\%s\\SourceData && pushd D:\\gitbash\\help && ECHO Please wait... && build.cmd"
            % (build_number, build_number),
            shell=True,
        )

        return out
