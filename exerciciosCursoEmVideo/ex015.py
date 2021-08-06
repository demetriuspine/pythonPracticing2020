km = float(input('Qual a quilometragem? '))
q = int(input('Qual a quantidade de dias? '))
km1 = km * 0.15
q1 = q * 60
t = km1 + q1
print('O valor do aluguel será de {:.2f} reais'.format(t))
