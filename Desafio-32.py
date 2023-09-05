#Para saber se o ano é bissexto ou não!
from datetime import date
ano = int(input('\033[36m Que ano quer analisar? Coloque o para analisar o ano atual: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    ano = date.today().year
    print('\033[36m O ano \033[35m{} \033[36m é BISSEXTO'.format(ano))
else:
    print('\033[36m O ano \033[35m{} \033[36m NÃO é BISSEXTO'.format(ano))