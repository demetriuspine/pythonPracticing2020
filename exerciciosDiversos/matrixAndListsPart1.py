#Implemente um programa que resolva a questão 1184 do Urionline, porém o exercício entregue deve sortear os números reais que preencherão a matriz. Copie e cole o código-fonte no campo a seguir.
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1184
import random as rd

oper=input('Digite a operação')
moper = oper.upper()
m = []

for i in range(12):
  m.append([])
  for j in range(12):
      x = rd.uniform(0,20)
      print('{:.1f}'.format(x))
      m[i].append(x)
if moper == 'S':
  s = 0
  c = 11
  for i in range(11,0,-1):
      for j in range(0,c):            
          s = s + m[i][j]
      c = c - 1
  print('A soma dos valores é: {:.1f}'.format(s))
elif moper == 'M':
  s = 0
  c = 11
  c2=0
  for i in range(11,0,-1):
      for j in range(0,c):            
          s = s + m[i][j]
          c2= c2 + 1
      c = c - 1       
  m=s/(c2)
  print('A média dos valores é: {:.1f}'.format(m))
else:
  print('Erro, digite S ou M')