nome = input()
print('Prazer, {:<20}!'.format(nome))   #acrescenta espaços depois
print('Prazer, {:>20}!'.format(nome))   #acrescenta espaços antes
print('Prazer, {:^20}!'.format(nome))   #acrescenta espaços antes e deppois
print('Prazer, {:=^20}!'.format(nome))  #acrescenta '='
print('Prazer, {:&^20}!'.format(nome))  #acrescenta '^'
print('Prazer, {:.5}!'.format(nome))    #limita a quantidade de caracteres