#Para saber o dobro,triplo e raiza quabrada de um número.
n = int(input('\033[32m Digite um número: '))
print('\033[31m Analisando seu número: {}.\n\033[32m O dobro é: {}\n\033[31m O triplo é: {}\n\033[32m e sua raiz quadrada é: {:.2f}'.format(n, (n*2), (n*3), (n**(1/2))))