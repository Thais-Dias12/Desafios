num = int(input('\033[33m Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('\033[31m Analisando o número {}'.format(num))
print('\033[32m Unidade: {}'.format(u))
print('\033[32m Dezena: {}'.format(d))
print('\033[32m Centena: {}'.format(c))
print('\033[32m Milhar: {}'.format(m))