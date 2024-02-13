import os
from compiler import *


BUILD_PATH = "C:/pa6autotests/Builds"

if __name__ == "__main__":
    compile = HelpCompiler()
    build_number = compile.show_current_build(BUILD_PATH)
    compile.excecute_script(build_number=build_number)
