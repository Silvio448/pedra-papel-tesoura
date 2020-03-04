# pedra-papel-tesoura
from random import randint
from time import sleep
while True:
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)
    print(''' Suas opções:
    [0] Pedra
    [1] Papel
    [2] Tesoura ''')
    jogador = int(input('Digite a sua opção: '))
    print('-=' * 15)
    print('Você escolheu', jogador)
    print('-=' * 15)
    print('Jo')
    sleep(1)
    print('Ken' )
    sleep(1)
    print('Po!!!')
    sleep(1)
    print('-=' * 15)
    print('Computador jogou: {}' .format(itens[computador] ))
    print('jogador jogou: {}' .format(itens[jogador]) )
    print('-=' * 15)
    if computador == 0: # computador jogou Pedra
        if jogador == 0:
            print('Empate')
            print('-=' * 15)
        elif jogador == 1:
            print('Jogador venceu')
            print('-=' * 15)
        elif jogador == 2:
            print('Computador venceu')
            print('-=' * 15) 
        else:
             print('Opção inválida')
             print('-=' * 15)        
    elif computador == 1: # computador jogou Papel
        if jogador == 0:
            print('Computador venceu')
            print('-=' * 15)
        elif jogador == 1:
            print('Empate')
            print('-=' * 15)
        elif jogador == 2:
            print('Jogador venceu')
            print('-=' * 15)
        else:
             print('Opção inválida')
             print('-=' * 15)     
    elif computador == 2:  # computador jogou Tesoura
        if jogador == 0:
            print('Jogador venceu')
            print('-=' * 15)
        elif jogador == 1:
            print('Computador venceu')
            print('-=' * 15)
        elif jogador == 2:
            print('Empate')
            print('-=' * 15)
        else:
             print('Opção inválida')
             print('-=' * 15)       
