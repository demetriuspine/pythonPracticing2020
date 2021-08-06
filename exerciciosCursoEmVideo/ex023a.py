num = int(input('Digite um número'))
u = num%10 # pega o resto da divisão por 10
d = num//10%10  #divide por 10, pega o inteiro, depois divide por 10 e pega o resto
c = num//100%10 #divide por 100, pega o inteiro, depois divide por 10 e pega o resto
m = num//1000%10 #divide por 1000, pega o inteiro, depois divide por 10 e pega o resto
print('{} unidades'.format(u))
print('{} dezenas'.format(d))
print('{} centenas'.format(c))
print('{} milhares'.format(m))