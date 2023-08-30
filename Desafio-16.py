dias = int(input('\033[36m Quantos dias alugados? '))
km = float(input('\033[36m Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('\033[36m O total a pagar é de \033[32mR${:.2f}'.format(pago))