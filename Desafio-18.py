from math import hypot
co = float(input('\033[33m Comprimento do cateto oposto: '))
ca = float(input('\033[33m Comprimento do cateto adjacente: '))
hi = hypot (co, ca)
print('\033[33m A hipotenusa vai medir \033[34m{:.2f}'.format(hi))