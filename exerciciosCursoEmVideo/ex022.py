nome = str(input()).strip()
print('Seu primeiro nome tem tem {} letras'.format((nome.find(' '))))
print('Seu nome completo, sem espaços tem {}'.format(len(nome)-nome.count(' ')))