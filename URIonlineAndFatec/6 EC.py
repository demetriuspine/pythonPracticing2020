a = float(input('Digite um valor: '))
if a == 0:
  print('{} é zero'.format(a))
else:
  if a < 0:
    print('{} é menor que zero'.format(a))
  else:
    print('{} é maior que zero'.format(a))