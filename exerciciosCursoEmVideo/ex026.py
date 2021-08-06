frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra O aparece {} vezes'.format(frase.count('O')))
print('A primeira letra O apareceu nao posição {}'.format(frase.find('O')+1))
print('A última letra O apareceu nao posição {}'.format(frase.rfind('O')+1)) #encontrar a partir da direita