from pyInputTester.tools.GeneratorInput.Types import *

def __split(string):
    pass

def get_int(line):
    pass

def get_str(line):
    pass

def get_float(line):
    pass

def get_bool(line):
    pass

def get_attrib(line, is_attribution=False):
    if not is_attribution:
        return get_variable(line)
    else:
        line = line.split('$')[1]
        name, value = [term.strip() for term in line.split('=')]

        if value[0] == '[' and value[len(value)-1] == ']':
            value = value.strip('[]')
            value = [element.strip() for element in value.split(',')]

        return (name, value)

def get_variable(line):
    pass

def read_for(line):
    pass

def read_while(line):
    pass