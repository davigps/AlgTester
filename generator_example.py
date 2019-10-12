from Tester import test
from random import randint, choice

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

colors = ['vermelho', 'laranja', 'amarelo', 'verde', 'azul']
cases = []

def get_name():
    n = randint(1, 5)
    name = ''
    for i in range(n):
        letter = choice(ALPHABET)
        name += letter
    return name

for i in range(randint(1, 10)):
    case = ''
    for i in range(randint(1, 10)):
        case += get_name() + ' ' + choice(colors) + '\n'
    case += 'fim\n'
    cases.append(case)

# Testing "hospital.py" with the generated cases.
test('hospital.py', cases)
