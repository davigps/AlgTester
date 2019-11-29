from pyInputTester.tools.Types import BooleanType, FloatType, StringType, IntegerType
# from Types import *
'''
Essas funções possuem a função de receber uma linha com os tipos de entradas necessários
e as limitações de cada entrada, ex: int(0<>100) bool(). E retorna as linhas preenchidas
com os valores, utilizando do mesmo exemplo acima, o valor retornado seria: 97 True ou
50 False, etc.
'''


def __split(string, line):
    ''' 
    Recebe como parâmetro os a string(int, str, bool, etc.) a ser procurada na linha passada,
    e retorna uma lista apenas com as especificações. No caso de inteiros '0<>100', strings
    'a...z', etc.
    '''
    att = ''
    config = []
    for i in range(len(line)-len(string)-1):
        for k in range(len(string)):
            att += line[i+k]
        if att == string:
            j = i+len(string)
            cont = -1
            while True:
                if line[j-1] == '(':
                    cont += 1
                if line[j-1] == ')':
                    if cont == 0:
                        break
                    else:
                        cont -= 1
                att += line[j]
                j += 1
            config.append(att)
        att = ''
    if string != 'bool':
        string += '('
        config = [att.strip(string) for att in config]
        config = [att.strip(')') for att in config]
    return config


def get_details(_type, __config):
    '''
    Recebe a lista com as configurações das entradas
    e faz os respectivos splits necessários para cada uma delas,
    de forma a deixar somente os limitadores 
    '''
    if _type == 'int':
        __config = [param.split('<>') for param in __config]
    elif _type == 'str':
        __config = [param.split(',') for param in __config]
        for params in __config:
            params[1] = params[1].strip()
            params[1] = params[1].split('...')
    elif _type == 'float':
        __config = [param.split(',') for param in __config]
        for params in __config:
            params[0] = params[0].split('<>')
            params[1] = params[1].strip()
    return __config


def get_int(line):
    '''
    Preenche a linha com números inteiros variados, de acordo com os limites
    passados.
    '''
    __config = __split('int', line)
    __config = get_details('int', __config)
    integer = IntegerType()
    for inputs in __config:
        param = integer.get_integer(int(inputs[0]), int(inputs[1]))
        string = 'int(' + inputs[0] + '<>' + inputs[1] + ')'
        line = line.replace(string, str(param), 1)

    return line


def get_str(line):
    '''
    Preenche a linha com strings variadas, de acordo com os limites passados
    '''
    __config = __split('str', line)
    __config = get_details('str', __config)
    string = StringType()
    for inputs in __config:
        param = string.get_string(int(inputs[0]), inputs[1][0], inputs[1][1])
        old_string = 'str(' + inputs[0] + ', ' + \
            inputs[1][0] + '...' + inputs[1][1] + ')'
        line = line.replace(old_string, param, 1)

    return line


def get_float(line):
    '''
    Preenche a linha com floats variados, de acordo com os limites passados
    '''
    __config = __split('float', line)
    __config = get_details('float', __config)
    float_type = FloatType()

    for __conf in __config:
        param = float_type.get_float(__conf[0][0], __conf[0][1], __conf[1])
        old_string = 'float(' + __conf[0][0] + '<>' + \
            __conf[0][1] + ', ' + __conf[1] + ')'
        line = line.replace(old_string, str(param), 1)

    return line


def get_bool(line):
    '''
    Preenche a linha com booleans variados
    '''
    __config = __split('bool', line)
    boolean = BooleanType()
    for inputs in __config:
        param = boolean.get_boolean()
        line = line.replace('bool()', str(param), 1)

    return line


def get_attrib(line):
    '''
    Return the variable name and its value, which exists in line. 
    '''
    line = line.split('$')[1]
    name, value = [term.strip() for term in line.split('=')]

    if value[0] == '[' and value[len(value)-1] == ']':
        value = value.strip('[]')
        value = [element.strip() for element in value.split(',')]

    return (name, value)


'''
----- Util Statements
'''


def get_seq(line):
    '''
    Get a sequence in line and return it with all "seq" occurrences replaced.
    Origin line: "seq(int(-10<>10), 3)"
    Returned line: "int(-10<>10) int(-10<>10) int(-10<>10)"
    Or maybe:
    Origin line: "seq(2, 5)"
    Returned line: "2 2 2 2 2"
    '''
    __config = __split('seq', line)
    for params in __config:
        item, times = [item.strip() for item in params.split(',')]
        string = ''
        for time in range(int(times)):
            space = ' ' if time != int(times) - 1 else ''
            string += item + space
        line = line.replace('seq(' + params + ')', string, 1)
    return line


'''
----- Local Tests
'''

if __name__ == "__main__":
    line = 'str(4, a...e) seq(int(0<>10), 5) bool() int(0<>100) float(3<>5, 2) str(3, a...b) int(5<>10)'
    line = get_seq(line)
    line = get_str(line)
    line = get_int(line)
    line = get_float(line)
    line = get_bool(line)
    print(line)
