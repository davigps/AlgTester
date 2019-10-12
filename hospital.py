# Davi Gomes Sousa - 119210408

prioridades = {'vermelho': 4, 'laranja': 3,
        'amarelo': 2, 'verde': 1, 'azul': 0}

cores = [0, 0, 0, 0, 0]
fila = []

def cadastra(fila, nome, prioridade):
    fila.append((nome, prioridade))

    i = len(fila) - 1
    while i > 0 and fila[i][1] <= fila[i - 1][1]:
        fila[i], fila[i-1] = fila[i-1], fila[i]
        i -= 1

def resumo(cores):
    for cor in prioridades:
        print('{}: {}'.format(cor, cores[prioridades[cor]]))
    print('---')

while True:
    paciente = input()
    if paciente == 'fim': break

    nome = paciente.split()[0]
    cor = paciente.split()[1]

    cadastra(fila, nome, prioridades[cor])

    cores[prioridades[cor]] += 1

for i in range(len(fila) - 1, -1, -1):
    paciente = fila[i]
    print(paciente[0])
print('---')

resumo(cores)

