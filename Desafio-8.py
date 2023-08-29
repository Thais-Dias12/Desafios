#Sabendo quantos metros tem em decimetros,centimetros e centimetros.
medida = float(input('\033[36m Digite uma distância em metros: '))
dm = medida / 10
cm = medida / 100
mm = medida / 1000
print('\033[36m A medida de\033[33m {:.0f}\033[36m metros, correspondem a:\033[33m {:.3f}\033[36m dm,\033[33m {:.2f}\033[36m cm,\033[33m {:.1f}\033[36m mm'.format( medida,dm, cm, mm))
#Quantos metros tem em decâmetros, hectômetro e quilômetro
dam = medida * 10
hm = medida * 100
km = medida * 1000
print('\033[33m A medida de \033[36m{:.0f}\033[33mm \033[33m corresponde a: \033[36m{:.0f}\033[33mkm, \033[36m{:.0f}\033[33mhm, \033[36m{:.0f}\033[33mdam.'.format(medida, km, hm, dam))