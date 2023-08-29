n1 = int(input('\033[7mDigite um valor: '))
n2 = int(input('\033[1;32mDigite outro valor: '))
s = n1 + n2
m = n1 - n2
M = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2 
print('\033[31m A soma é: {}'.format(s))
print('\033[32m A subitração é: {}'.format(m))
print('\033[33m A multiplicação é: {}'.format(M))
print('\033[34m A divisão é: {:.3f}'.format(d))
print('\033[35m Divisão real é: {}'.format(di))
print('\033[1;36m O resto da divisão é: {}'.format(r))
print('\033[37m Potencia é: {}'.format(e)) 