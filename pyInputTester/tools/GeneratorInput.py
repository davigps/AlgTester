from pyInputTester.tools.__statements__ import *
from random import choice

class GeneratorInput:

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

    def __get_input_lines(self):
        input_lines = []
        declaration = False
        for line in self.__file:
            if declaration:
                input_lines.append(line)
            elif line.strip() == 'input:':
                declaration = True
        return input_lines

    def __resolve_variables(self, lines):
        lines = lines[:]
        
        for name in self.variables.keys():

            value = self.variables[name]

            if type(value) == list:
                value = choice(value)

            for i in range(len(lines)):
                lines[i] = lines[i].replace(name, str(value))

        return lines

    def __get_scope(self, scope, lines):
        start = None
        for i in range(len(lines)):
            if scope in lines[i]:
                start = i
                break
        
        declaration_line = lines[start]
        param = declaration_line.split(scope)[1].split(')')[0]

        i = start + 1
        scope_lines = []

        stack = [True]

        while len(stack) > 0:
            if lines[i].strip() == '}': stack.pop()
            else:
                if '{' in lines[i]: stack.append(True)

                scope_lines.append(lines[i])
                i += 1
        return {
            "start": start,
            "end": i,
            "scope": scope_lines,
            "param": param
        }

    def __scope_exists(self, scope, lines):
        for line in lines:
            if scope in line:
                return True
        return False

    def __resolve_for(self, lines):
        lines = lines[:]
        
        while self.__scope_exists('for(', lines):
            for_scope = self.__get_scope('for(', lines)
            
            for i in range(len(for_scope["scope"])):
                lines.pop(for_scope["start"])
            
            for i in range(int(for_scope["param"])):
                for j in range(len(for_scope["scope"]) - 1, -1, -1):
                    lines.insert(for_scope["start"], for_scope["scope"][j])

        return lines
    
    def __resolve_while(self, lines):
        lines = lines[:]
        
        while self.__scope_exists('whilenot(', lines):
            while_scope = self.__get_scope('whilenot(', lines)
            # To do

        return lines

    def generate_inputs(self):

        for case in range(self.number_of_cases):
            lines = self.__get_input_lines()

            self.search_variables()
            lines = self.__resolve_variables(lines)
            lines = self.__resolve_for(lines)
            lines = self.__resolve_while(lines)

            case = self.__read_lines(lines)
            self.inputs_created.append(case)

        return self.inputs_created
