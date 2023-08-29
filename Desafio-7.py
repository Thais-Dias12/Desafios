#Calculo das 4 notas do aluno, para saber sua média.
n1 = float(input('\033[35m Digite sua primeira nota: '))
n2 = float(input('\033[36m Digite sua segunda nota: '))
n3 = float(input('\033[35m Digite sua terceira nota: '))
n4 = float(input('\033[36m Digite sua quarta nota: '))
m = (n1 + n2 + n3 + n4)/4
print('\033[35m A média do aluno é: \033[36m{}'.format(m))
#Estrutura para escolhas, se a média for maior ou igual vai aparecer a primeira mensagem.
if m >= 7:
 print('\033[32m Parabéns, você passou!!!')
#Caso for menor vai aparecer essa mensagem.
elif m < 7:
 print('\033[31m Infelizmente, você não passou!!!')
