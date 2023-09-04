import random
a1 = str(input('\033[36m Digite o primeiro nome:\033[32m '))
a2 = str(input('\033[36m Digite o segundo nome:\033[32m '))
a3 = str(input('\033[36m Digite o terceiro nome:\033[32m '))
a4 = str(input('\033[36m Digite o quarto nome:\033[32m '))
list = [a1, a2, a3, a4]
escolhido = random.choice(list)
print('\033[36m O aluno escolhido foi \033[32m{}'.format(escolhido))
