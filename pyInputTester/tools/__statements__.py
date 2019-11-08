<<<<<<< HEAD
from pyInputTester.tools.Types import *
#from Types import *
=======
# from pyInputTester.tools.Types import *
from Types import *
>>>>>>> 84772880441058b1dbf2209a38b791dc6828744f

def __split(string, line):
    att = ''
    config = []
    for i in range(len(line)-len(string)-1):
        for k in range(len(string)):
            att += line[i+k] 
        if att == string:
            j = i+len(string)
            while True:
                if line[j-1] == ')': break
                att += line[j]
                j += 1
            config.append(att)
        att = ''
    if string != 'bool':
        string += '('
        config = [att.strip(string) for att in config]
        config = [att.strip(')') for att in config]
    
    return config

def get_int(line):
    __config = __split('int', line)
    __config = [att.split('<>') for att in __config]
    integer = IntegerType()
    for inputs in __config:
        param = integer.get_integer(int(inputs[0]), int(inputs[1]))
        string = 'int(' + inputs[0] + '<>' + inputs[1] +')'
        line = line.replace(string, str(param))
    
    return line

def get_str(line):
    __config = __split('str', line)
    __config = [att.split(',') for att in __config]
    string = StringType()
    for inputs in __config:
        inputs[1] = inputs[1].strip()      
        inputs[1] = inputs[1].split('...')
        param = string.get_string(int(inputs[0]), inputs[1][0], inputs[1][1])
        old_string = 'str(' + inputs[0] + ', ' + inputs[1][0] + '...' + inputs[1][1] + ')' 
        line = line.replace(old_string, param)

    return line

def get_float(line):
    __config = __split('float', line)
    __config = [att.split(',') for att in __config]
    for __conf in __config:
        __conf[0] = __conf[0].split('<>')
        __conf[1] = __conf[1].strip()
    
    float_type = FloatType()

    for __conf in __config:
        param = float_type.get_float(__conf[0][0], __conf[0][1], __conf[1])
        old_string = 'float(' + __conf[0][0] + '<>' + __conf[0][1] + ', ' + __conf[1] + ')'
        line = line.replace(old_string, str(param))
    
    return line

def get_bool(line):
    __config = __split('bool', line)
    boolean = BooleanType()
    for inputs in __config:
        param = boolean.get_boolean()
        line = line.replace('bool()', str(param))

    return line

def get_attrib(line):
    line = line.split('$')[1]
    name, value = [term.strip() for term in line.split('=')]

    if value[0] == '[' and value[len(value)-1] == ']':
        value = value.strip('[]')
        value = [element.strip() for element in value.split(',')]

    return (name, value)

<<<<<<< HEAD
        return (name, value)

=======
>>>>>>> 84772880441058b1dbf2209a38b791dc6828744f
def get_seq(line):
    # To do
    pass

if __name__ == "__main__":
    line = 'str(4, a...e) bool() int(0<>100) str(10, a...b) float(3<>5, 2) str(3, a...b) int(5<>10)'
    line = get_str(line)
    line = get_int(line)
    line = get_float(line)
    line = get_bool(line)
    print(line)
