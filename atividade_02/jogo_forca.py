import sys
import random

membros_corpo = (
    'Perna esquerda',
    'Perna direita',
    'Braço esquerdo',
    'Braço direito',
    'Corpo',
    'Cabeça'
)

palavras = (
    'desenvolvimento',
    'tecnologia',
    'lógica de programação',
    'python',
    'sistemas de informação'
)

def escolher_palavra():
    return palavras[random.randint(0, len(palavras)-1)]


def exibir_forca(n_tentativas):
    print('\nExibindo atual da forca:\n')

    if n_tentativas == 0:
        print('Seu boneco está inteiro!\n\n')

    else:
        print('Seu boneco está sem os membros: ')
        
        for i in range(0, n_tentativas):
            print(' - ' + membros_corpo[i])
        
        print('\n')

        if len(membros_corpo) == n_tentativas:
            raise Exception('Você perdeu o corpo inteiro!')


def jogar():
    tentativas = 0
    letras_tentadas = []
    lista_caracteres = {}
    palavra = escolher_palavra()

    for indice, caractere in enumerate(palavra):
        if caractere == '-':
            lista_caracteres[caractere + str(indice)] = '-'
            continue
        
        if caractere == ' ':
            lista_caracteres[caractere + str(indice)] = ' '
            continue

        lista_caracteres[caractere + str(indice)] = '_'


    print('Boas vindas!')

    encerrado = False
    
    while not encerrado:
        try:
            exibir_forca(tentativas)
        except Exception as e:
            encerrado = True
            print(e)
            continue
        
        print('A palavra é: ' + ' '.join(lista_caracteres.values()))
        letra_jogada = input('Advinhar uma letra: ')

        if letra_jogada in letras_tentadas:
            print('Letra já foi tentada!')
            continue
        
        letras_tentadas.append(letra_jogada)

        if letra_jogada not in palavra:
            tentativas += 1
            continue
        
        for caractere in lista_caracteres:
            if caractere.startswith(letra_jogada):
                lista_caracteres[caractere] = letra_jogada
        
        if '_' not in lista_caracteres.values():
            print('Você ganhou! A palavra é ' + ''.join(lista_caracteres.values()))
            encerrado = True
    
    print('Obrigado por jogar!')

jogar()
