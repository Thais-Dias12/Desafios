#Multa de velocidade
velocidade = float(input('\033[33m Qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('\033[31m MUlTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('\033[33m Você deve pagar uma multa de \033[31m R${:.2f}\033[33m !'.format(multa))
    print('\033[33m Tenha um bom dia! Dirija com segurança!')