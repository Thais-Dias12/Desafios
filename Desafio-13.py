#Calculando  aumento do salario do funcionario:
salario = float(input('\033[35m Qual é o salário do funcionario? R$'))
if salario <= 1200:
 print('\033[35m O salário do funcionario \033[32mR${:.2f}\033[35m, com 15% de aumento, passa a receber \033[32mR${:.2f}'.format(salario, salario + (salario * 15 / 100)))
elif salario <= 1300:
 print('\033[35m O salário do funcionario \033[32mR${:.2f}\033[35m, com 25% de aumento, passa a receber \033[32mR${:.2f}'.format(salario, salario + (salario * 25 / 100)))
elif salario <= 1400: 
 print('\033[35m O salário do funcionario \033[32mR${:.2f}\033[35m, com 35% de aumento, passa a receber \033[32mR${:.2f}'.format(salario, salario + (salario * 35 / 100)))
elif salario <= 1500:
 print('\033[35m O salário do funcionario \033[32mR${:.2f}\033[35m, com 45% de aumento, passa a receber \033[32mR${:.2f}'.format(salario, salario + (salario * 45 / 100)))
elif salario <= 1600:
 print('\033[35m O salário do funcionario \033[32mR${:.2f}\033[35m, com 50% de aumento, passa a receber \033[32mR${:.2f}'.format(salario, salario + (salario * 50 / 100)))