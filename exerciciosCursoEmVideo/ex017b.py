from math import hypot
cat1 = float(input('Digite o valor do cateto adjascente: '))
cat2 = float(input('Digite o valor do cateto oposto: '))
hip = hypot(cat1, cat2)
print('O valor da hipotenusa é: {}'.format(hip))
