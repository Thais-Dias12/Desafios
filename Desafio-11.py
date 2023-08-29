#largura da parede e altura, para saber quantos litros de tinta vai ser usado.
larg = float(input('\033[34m Largura da parede:\033[31m '))
alt = float(input('\033[34m Altura da parede:\033[31m '))
area = larg * alt
print('\033[34m Sua parede tem a dimensão de \033[31m{:.0f}x{:.0f} \033[34me sua área é de \033[31m{:.0f}m².'.format(larg, alt, area))
tinta = area / 2
print('\033[34m Para pintar essa parede é necessario \033[31m{:.0f}L \033[34m de tintas.'.format(tinta))