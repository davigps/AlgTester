from pyInputTester.tools.GeneratorInput.__statements import get_attrib, get_bool, get_float, get_int, get_str, get_variable, read_for, read_while

class GeneratorInput:

    inputs = []

    def __init__(self, number_of_cases, path_to_file='.test'):
        self.number_of_cases = number_of_cases
        self.__file = open(path_to_file, 'r').readlines()
        self.inputs_created = []

        self.__key_words = [
            '$', 'while not ', 'for ',
            'int(', 'float(', 'bool()', 'str('
        ]
        self.__statements = {
            'int(': get_int, 'float(': get_float, 'bool(': get_bool,
            'str(': get_str, '$': get_attrib, 'for ': read_for,
            'while not ': read_while
        }

        self.variables = {}

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
                name, value = self.__statements['$'](line)
                self.variables[name] = value

    def generate_inputs(self):
        self.search_variables()

        for case in range(self.number_of_cases):
            case = ''
            is_input = False
            for line in self.__file:
                line = line.strip()
                if line == 'input:':
                    is_input = True
                elif is_input:
                    keys = self.__get_statements(line)
                    for key in keys:
                        value = self.__statements[key](line)




        return self.inputs_created
