#Jogo de adivinhação! com computador.
from random import randint
computador = randint(0, 5) #Computador esta "Pensando"
print('-=-'* 10)
print('\033[33m Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'* 10)
jogador = int(input('\033[34m Em que número eu pensei? ')) #Jogador tentando adivinhar
print('\033[33m Pensei no número \033[34m{}'.format(computador))
if jogador == computador:
    print('\033[32m PARABÉNS!!! Você conseguiu me vencer!')
else:
    print('\033[31m GANHEI! Eu pensei no número \033[34m{}\033[31 me não no \033[34m{}\033[31m!'.format(computador, jogador))