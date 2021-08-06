#Faça um programa que sorteie e guarde em uma lista 100 números inteiros de -200 a 200. No final, mostre todas as posições da lista que armazenam um valor positivo e par.

import random as rd

lista = []

for i in range(99):
  x = rd.randint(-200, 200)
  lista.append(x)

print(lista)

for j in range(99):
  if lista[j] > 0:
    if lista[j]%2 == 0:
      print(f'O valor da posição {j} é um valor positivo e par')