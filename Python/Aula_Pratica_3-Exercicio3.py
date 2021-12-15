# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh
# consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios.

print('Cálculo de Energia Elétrica Utilizada!')
print('R - Residências')
print('I - Indústrias')
print('C - Comércios')

un = input('Por favor, informe o tipo de instalação: ')
kwh = float(input('Informe a quantidade de kWh consumida no mês: '))

if un == 'R' or un == 'r':
    if kwh <= 500:
        preco = 0.4
    else:
        preco = 0.65

elif un == 'C' or un == 'c':
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60

elif un == 'I' or un == 'i':
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.60

else:
    print('Instalação Inválida!')

print('Total à pagar: {}.' .format(kwh * preco))