#Programa para saber se o número é par ou impar.
numero = int(input('\033[35m Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('\033[35m O número \033[32m{} \033[35m é \033[34mPAR'.format(numero))
else:
    print('\033[35m O número \033[32m{} \033[35m é \033[31mIMPAR'.format(numero))