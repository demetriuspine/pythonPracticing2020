p1 = float(input('P1= '))
p2 = float(input('P2= '))
p3 = float(input('P3= '))
p4 = float(input('P4= '))
m = (2*p1+2*p2+3*p3+3*p4)/10
if m >= 7:
  print('Aprovado')
else:
  if m < 5:
    print('Reprovado')
  else:
    ex = float(input('Exame: '))
    mf = (m + ex)/2
    if mf >= 7:
      print('Aprovado')
    else:
      print('Reprovado')
