from pyInputTester.tools.Types import *
# from Types import *

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
    if string != 'float':
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

if __name__ == "__main__":
    line = 'str(4, a...e) int(0<>100) str(10, a...b) float() str(3, a...b) int(5<>10)'
    line = get_str(line)
    line = get_int(line)
    print(line)