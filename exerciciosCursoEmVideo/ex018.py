import math
ang = float(input('Digite o valor do ângulo: '))
a = math.radians(ang)
sen = math.sin(a)
cos = math.cos(a)
tan = math.tan(a)
print('O seno é: {:.2f}\nO cosseno é: {:.2f}\nE a tangente é: {:.2f}'.format(sen, cos, tan))
