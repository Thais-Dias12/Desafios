#Saber se três retas formam um triangulo
print('-=' * 20)
print('\033[33m Analisador de triângulos')
print('-=' * 20)
r1 = float(input('\033[32m Primeiro segmento: '))
r2 = float(input('\033[32m Segundo segmento: '))
r3 = float(input('\033[32m Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +  r2:
    print('\033[34m Os segmentos acima PODEM FORMAR triângulo!')
else: 
    print('\033[31m Os segmentos acima NÃO PODEM FORMAr triângulo')