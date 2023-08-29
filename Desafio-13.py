salario = float(input('\033[35m Qual é o salário do funcionario? R$'))
aumento = salario + (salario * 15 / 100)
print('\033[35m O salário do funcionario \033[32mR${:.2f}\033[35m, com 15% de aumento, passa a receber \033[32mR${:.2f}'.format(salario, aumento))