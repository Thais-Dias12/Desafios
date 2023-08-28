nome = input('\033[34mDigite seu nome:\033[34m ')
cores = {'vermelho': '\033[31m', 'azul': '\033[34m'}
print(f'{cores["azul"]}É um prazer te conhecer,{cores["azul"]} {cores["vermelho"]}{nome}{cores["vermelho"]}!')
