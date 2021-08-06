a = int(input('Qual a idade do cliente? '))
b = float(input('Qual o preço do produto? '))
if a >= 90:
    print('O valor a ser pago será de R${:.2f}'.format(b*0.5))
elif a > 80 and a < 90:
    print('O valor a ser pago será de R${:.2f}'.format(b*0.6))
elif a > 70 and a <= 80:
    print('O valor a ser pago será de R${:.2f}'.format(b*0.7))
elif a > 60 and a <= 70:
    print('O valor a ser pago será de R${:.2f}'.format(b*0.8))
else:
    print('O produto não terá desconto e seu preço será de R${:.2f}'.format(b))