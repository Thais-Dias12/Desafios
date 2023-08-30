c = float(input('\033[36m Informe a temperatura em ºC: '))
f = ((9*c)/5)+32
print('\033[36m A temperatura de \033[33m{:.0f}ºC\033[36m, corresponde \033[33m{:.0f}ºF\033[36m! '.format(c, f))