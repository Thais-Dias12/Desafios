#Separador de nomes
n = str(input('\033[33m Digite seu nome completo: ')).strip()
nome = n.split()
print('\033[31m Muito prazer em te conhecer!')
print('\033[31m Seu primeiro nome é \033[33m{}'.format(nome[0]))
print('\033[31m ultimo nome é \033[33m{}'.format(nome[len(nome)-1]))