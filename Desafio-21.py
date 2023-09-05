import random
a1 = str(input('\033[31m Primeiro aluno: '))
a2 = str(input('\033[32m Segundo aluno: '))
a3 = str(input('\033[33m Terceiro aluno: '))
a4 = str(input('\033[34m Quarto aluno: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('\033[35m A ordem de apresentação será: ')
print(lista)