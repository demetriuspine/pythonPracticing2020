frase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. '
originalFrase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. '
frase1 = frase.replace(' ', '/')
frase2 = originalFrase.replace(' ', '/')
print(frase1)
print(frase.split()) # divide a string em palavras (divide pelos espaços) com uma nova lista
print(frase1.split('/')) # ao colocar um caractere, ele usa como referencia para dividir
fraseArray = frase2.split('/')
print('/'.join(fraseArray)) #junta os elementos de uma lista em uma string com um determinado caractere