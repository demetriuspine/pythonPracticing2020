conta = 1 #ponmto de partida
while conta <= 5:
  altura = float(input("Altura"))
  peso = float(input("Peso"))
  imc = peso / (altura ** 2)
  print("IMC %f" % imc)
  conta += 1          # (conta = conta+1)

