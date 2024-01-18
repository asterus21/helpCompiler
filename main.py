import os
import subprocess
import sys

build_path = 'C:\\pa6autotests\\Builds'

# print(os.listdir(path=build_path)[0])

def show_current_build(build_path: str) -> str:
   
   """ The function is to accept a path to an auto-test build 
   and returns a first (a single item) of the list. """  

   global build_number
   build_number = os.listdir(path=build_path)[0]
   return build_number

# print(script_text % (build_number, build_number))

def excecute_script(build_number: str) -> None:

    """ The function is to accept a build number as a string
    to execute a Command Line (CMD) script. """

    process = subprocess.Popen("C:\\Windows\\System32\\cmd.exe " + "@ECHO OFF && pushd D:\\pa_config && set COMLICBITSPATH=D:\\pa_config\\comlicbits.h && pushd C:\\pa6autotests\\Builds\\%s\\SourceData && set SOURCEDATA=C:\\pa6autotests\\Builds\\%s\\SourceData && pushd D:\\gitbash\\help && ECHO Please wait... && build.cmd" % (build_number, build_number), stdout=subprocess.PIPE)

    for line in process.stdout:
        sys.stdout.write(line)

show_current_build(build_path)
excecute_script(build_number)

# use a different method, e.g. subprocess
