import math
angulo = float(input('\033[34m Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('\033[34m O ângulo de \033[33m{:.0f}\033[34m tem p SENO de \033[33m{:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('\033[34m O ângulo de \033[33m{:.0f}\033[34m tem COSSENO de \033[33m{:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('\033[34m O ângulo de \033[33m{:.0f}\033[34m tem a TANGENTE de \033[33m{:.2f}'.format(angulo, tangente))