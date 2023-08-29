#verificando descontos!
produto = float(input('\033[32m Qual o valor do produto? \033[31mR$'))
d1 = produto - (produto * 5 / 100)
d2 = produto - (produto * 25 / 100) 
d3 = produto - (produto * 50 / 100)
print('\033[32m O produto que custa \033[31mR${:.2f} \033[32m na promoção custa com 5% desconto fica: \033[31mR${:.2f}, \033[32m com desconto de 25% fica: \033[31mR${:.2f},\033[32m e com desconto de 50% fica: \033[31m R${:.2f}'.format(produto, d1, d2, d3))