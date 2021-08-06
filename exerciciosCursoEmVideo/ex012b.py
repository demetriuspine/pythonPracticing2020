p = float(input('Qual o preço do produto? '))
d = float(input('Quanto será o percentual de desconto?'))
per = (100-d)/100
print('O preço com desconto de %i %% ficará em %.2f Reais'%(d, per*p))
