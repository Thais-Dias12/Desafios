#Um programa para ver qual dos três números é maior e qual é o menor.
a = int(input('\033[36m Primeiro número: '))
b = int(input('\033[35m Segundo número: '))
c = int(input('\033[34m Terceiro número: '))
#Verificando quem é o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and b<c:
    menor = c
print('\033[33m O menor valor digitado foi \033[31m{}'.format(menor))
#verificando qual é maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('\033[32m O maior valor digitado foi \033[31m{}'.format(maior))