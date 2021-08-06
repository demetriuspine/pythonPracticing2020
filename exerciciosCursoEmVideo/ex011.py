a = float(input('Qual a altura da parede (em metros?) '))
l = float(input('E a largura (em metros)? '))
A = float(a*l)
t = 2
lt = A/t
print('A sua parece tem {} m², logo você precisará de no mínimo {} litros de  para pintá-la'.format(A, lt))
