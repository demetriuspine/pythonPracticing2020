teste = 'Nobody expects the spanish inquisition'
print(len(teste))       #comprimento
print(teste.count('e')) #contar a quantidade de 'e'
print(teste.count('e',0,14)) #contar a quantidade de 'e', entre 0 e 14, excluindo o 14
print(teste.find('p')) #mostra aonde começa a frase ou letra
print('pau' in teste) #verifica se existe a palavra dentro de teste
print(teste.replace('spanish', 'portuguese')) #substitui
print(teste.upper()) #transforma tudo em maiusculo
print(teste.lower()) #transforma tudo em minusculo
print(teste.capitalize()) #transforma só o primeiro em maiusculo, o resto em minusculo
print(teste.title()) #transforma a primeira letra de cada palavra em maisuculo
frase = '   AH mlk  '
print(frase.strip()) # remove os espaços inuteis do inicio e do fim
print(frase.rstrip()) #remove os espaços da direita
print(frase.lstrip()) #remove os espaços da esquerda