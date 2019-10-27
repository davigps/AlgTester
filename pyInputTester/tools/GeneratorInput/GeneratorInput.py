from pyInputTester.tools.GeneratorInput.__statements import *

class GeneratorInput:
    inputs = []

    def __init__(self, number_of_cases, path_to_file='.test'):
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
        print(self.variables)
        # for line in self._file:
        #     self.inputs.append(line.split())
        
        # for _input in self.inputs:
        #     if _input[0].lower() == 'int' or _input[0].lower() == 'float':
        #         _input[1] = _input[1].split('<>')

        #     elif _input[0].lower() == 'str':
        #         _input[2] = _input[2].split('...')
       
        # for _input in self.inputs:

        #     if _input[0].lower() == 'int':
        #         variable = IntegerType(int(_input[1][0]), int(_input[1][1])).get_integer()
        #     elif _input[0].lower() == 'float':
        #         variable = FloatType(float(_input[1][0]), float(_input[1][1]), 2).get_float()
        #     elif _input[0].lower() == 'bool':
        #         variable = BooleanType().get_boolean()
        #     elif _input[0].lower() == 'str':
        #         variable = StringType(int(_input[1]), _input[2][0], _input[2][1]).get_string()
                
        #     self.inputs_created.append(variable)
        # return self.inputs_created

