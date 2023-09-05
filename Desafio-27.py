frase = str(input('\033[34m Digite uma frase: ')).upper()
print('\033[31m A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('\033[31m A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('\033[31m A ultima letra A aparece na posição {}'.format(frase.rfind('A')+1))