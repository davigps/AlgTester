from pyInputTester.tools.__statements__ import *

class GeneratorInput:

    inputs = []

    def __init__(self, number_of_cases, path_to_file='.test'):
        self.number_of_cases = number_of_cases
        self.__file = open(path_to_file, 'r').readlines()

        self.__key_words = [
            'int(', 'float(', 
            'bool()', 'str('
        ]
        self.__statements = {
            'int(': get_int, 'float(': get_float, 
            'bool(': get_bool, 'str(': get_str
        }

        self.variables = {}
        self.inputs_created = []

    def __get_statements(self, line):
        keys = []
        for key in self.__key_words:
            if key in line:
                keys.append(key)
        return keys

    def search_variables(self):
        for line in self.__file:
            line = line.strip()
            if line == 'input:': return None
            keys = self.__get_statements(line)
            if len(keys) == 1 and keys[0] == '$':
                name, value = get_attrib(line)

                keys = self.__get_statements(value)
                for key in keys:
                    value = self.__statements[key](value)

                self.variables[name] = value

    def __read_lines(self, lines):
        case = ''
        for line in lines:
            line = line.strip()
            
            keys = self.__get_statements(line)
            for key in keys:
                line = self.__statements[key](line)
                
            line += '\n'
        case += line
        return case

    def generate_inputs(self):

        for case in range(self.number_of_cases):
            lines = self.__get_input_lines()

            self.search_variables()
            lines = self.__resolve_variables(lines)
            lines = self.__resolve_for(lines)
            lines = self.__resolve_while(lines)

            case = self.__read_lines(self.__file)
            self.inputs_created.append(case)

        return self.inputs_created
