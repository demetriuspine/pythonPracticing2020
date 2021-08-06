a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
if b == 0:
  print('Impossível dividir')
else:
  d = int(a/b)
  print('A divisão entre {} e {} é {}'.format(a, b, d))
