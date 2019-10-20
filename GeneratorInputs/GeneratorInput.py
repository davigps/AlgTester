from StringType import StringType
from IntegerType import IntegerType
from BooleanType import BooleanType
from FloatType import FloatType

class GeneratorInput:
    inputs = []    
    def __init__(self, inputs = []):
        self.file = open('.test', 'r').readlines()
        self.inputscreated = inputs

    def generate_inputs(self):
        for line in self.file:
            self.inputs.append(line.split())
        
        for input_ in self.inputs:
            if input_[0].lower() == 'int' or input_[0].lower() == 'float':
                input_[1] = input_[1].split('<>')

            elif input_[0].lower() == 'str':
                input_[2] = input_[2].split('..')
       
        for input_ in self.inputs:

            if input_[0].lower() == 'int':
                variable = IntegerType(int(input_[1][0]), int(input_[1][1])).getInteger()
            elif input_[0].lower() == 'float':
                variable = FloatType(float(input_[1][0]), float(input_[1][1]), 2).getFloat()
            elif input_[0].lower() == 'bool':
                variable = BooleanType().getBoolean()
            elif input_[0].lower() == 'str':
                variable = StringType(int(input_[1]), input_[2][0], input_[2][1]).getString()
                
            self.inputscreated.append(variable)

