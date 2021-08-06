tab = int(input('Digite o valor da tabuada: '))
for x in range(1, 11):
  print(f'{x:^3}x{tab:>2} = {x*tab:>2}')
