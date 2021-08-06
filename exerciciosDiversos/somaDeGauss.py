numeroMaximo = int(input())
def somaDeGauss(numeroMaximo):
  i = 1
  soma = 0
  while i <= numeroMaximo:
    soma = soma + i
    i = i + 1
  return soma
print(somaDeGauss(numeroMaximo))