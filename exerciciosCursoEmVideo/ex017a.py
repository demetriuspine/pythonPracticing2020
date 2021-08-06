import math
cat1 = float(input('Informe o cateto adjascente: '))
cat2 = float(input('Informe o cateto oposto: '))
hip = math.hypot(cat2, cat1)
print('O comprimento da hipotenusa é: {}'.format(hip))
