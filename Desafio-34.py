#Qual salario de um funcionario  e calcular o seu aumento.
salario = float(input('\033[33m Qual salário do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario +(salario * 10 / 100)
print('\033[33m Quem quanhava \033[36mR${:.2f} \033[33m passa a ganhar agora \033[36mR${:.2f}'.format(salario, novo))