import sys


# Controller
def soma(n1, n2):
    return n1+n2


def sub(n1, n2):
    return n1-n2


def multi(n1, n2):
    return n1*n2


def div(n1, n2):
    return n1/n2


def despedida():
    print('Adeus e hello world!')
    sys.exit()


# Adapter
def call_operation(n1, n2, operation):
    returnValue = None

    match operation:
        case 1:
            returnValue = soma(n1, n2)
        case 2:
            returnValue = sub(n1, n2)
        case 3:
            returnValue = multi(n1, n2)
        case 4:
            returnValue = div(n1, n2)
    
    return returnValue


# View: Menu
def select_operation():
    print('\n Menu de opções: \n')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair \n')

    return int(input('Qual operação deseja realizar? '))


# View: Validation
def validate_operation(op):
    if (op is None):
        raise Exception('Invalid input')

    if (op < 1 or op > 5):
        raise Exception('Invalid input')
        
    if (op == 5):
        despedida()
    
    return op


# View: Main
operation = None
while(operation != 5):
    try:
        operation = validate_operation(select_operation())

        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))

        print('O resultado é: ', call_operation(n1, n2, operation))

    except Exception as e:
        print('Escolha apenas números de 1 a 5!!!')
