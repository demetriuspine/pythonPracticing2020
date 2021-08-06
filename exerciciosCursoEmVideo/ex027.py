nome = str(input('Digite seu nome: ')).strip()
n = nome.split()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1])) #-1 pq num nome com 3 palavras,o cumprimento é 3 mas a posição é 0, 1 e 2