# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar:
# adição (+), subtração ( (--), multiplicação (*) ou divisão (/). Exiba na tela o resultado da operação desejada.
print('Calcule!')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')

op = input('Digite qual operação você deseja fazer: ')
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

if op == '+':
    res = x + y
    print('O resultado da adição de {} com {} é de {}.' .format(x,y,res))
elif op == '-':
    res = x - y
    print('O resultado da subtração {} com {} é de {}.' .format(x,y,res))
elif op == '*':
    res = x * y
    print('O resultado da multiplicação de {} por {} é de {}.' .format(x,y,res))
elif op == '/':
    res = x // y
    print('O resultado da divisão {} por {} é de {}.' .format(x,y,res))