numero = int(input())
outroNumero = int(input())
operacao = input()
def calculadoraAdicaoSubtracao(numero, outroNumero, operacao):
  if operacao == '+':
    resultado = numero + outroNumero
  elif operacao == '-':
    resultado = numero - outroNumero
  else:
    resultado = 0
  return resultado
print(calculadoraAdicaoSubtracao(numero, outroNumero, operacao))