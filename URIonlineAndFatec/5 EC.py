a = float(input('Dígite um valor: '))
b = float(input('Digite outro valor: '))
if a == b:
  print('{} e {} São iguais'.format(a, b))
else:
  if a < b:
    print('{} é maior\n{} é menor'.format(b, a))
  else:
    print('{} é maior\n{} é menor'.format(a, b))
