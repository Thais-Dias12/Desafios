#verificando produto com desconto, e com aumento
produto = float(input('\033[33mDigite o valor do produto: '))
f1 = produto - (produto * 10 /100)
f2 = produto + (produto * 8 / 100)
print('\033[33mO produto custa: R$\033[32m{:.2f}'.format(produto))
print('\033[33mpagando a vista você recebe 10% de desconto, que fica: R$\033[32m{:.2f}'.format(f1)) 
print('\033[33mAgora se for parcelado tera um aumento de 8%, ficando: R$\033[32m{:.2f}'.format(f2))