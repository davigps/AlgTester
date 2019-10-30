from pyInputTester.tools.statements import *

class GeneratorInput:

    inputs = []

    def __init__(self, number_of_cases, path_to_file='.test'):
        self.number_of_cases = number_of_cases
        self.__file = open(path_to_file, 'r').readlines()

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
                name, value = self.__statements['$'](line, is_attribution=True)
                self.variables[name] = value

    def __get_input_declaration(self):
        
        class Input_Declaration:

            def __init__(self, file):
                self.repeat_times = 1
                self.lines = []
            
            def __read_input_declaration(self, file):
                pass
        
        return Input_Declaration(self.__file)

    def __read_lines(self, lines, read_times):
        case = ''
        for time in range(read_times):
            for line in lines:
                line = line.strip()
                
                keys = self.__get_statements(line)
                for key in keys:
                    line = self.__statements[key](line)
                    
                line += '\n'
            case += line
        return case

    def generate_inputs(self):
        self.search_variables()

        for case in range(self.number_of_cases):
            case = ''

            input_declaration = self.__get_input_declaration()

            case += self.__read_lines(input_declaration, 1)
            
            self.inputs_created.append(case)

        return self.inputs_created
