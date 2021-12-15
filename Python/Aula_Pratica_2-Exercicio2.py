# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a
# quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por
# dia e R$ 0,15 por KM rodado.

km = int(input('Coloque a quantidade de KM percorridos: '))
d = int(input('Coloque a quantidade de dias alugados: '))

preco = 60 * d + 0.15 * km

print('KM = {}; Dias: {}' .format(km, d))
print('Valor a ser pago: {}' .format(preco))
