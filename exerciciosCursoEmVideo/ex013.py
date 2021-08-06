s = float(input('Qual o valor do seu salário? '))
d = float(input('Qual o percentual de seu aumento?' ))
per = s * ((d/100)+1)
print('O seu novo salário com o aumento de {}% será de {:.2f} Reais'.format(d, per))

