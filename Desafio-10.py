#Sabendo com quantos reais, você teria de dollars.
real = float(input('\033[35m Quantos reais você tem em sua carteira? R$'))
dollar = real / 4.87
print('\033[35m Com R${:.2f}, Você pode comprar US${:.2f}'.format(real, dollar))