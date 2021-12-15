# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar:
# adição (+), subtração ( (--), multiplicação (*), divisão (/) e sair . Exiba na tela o resultado da operação desejada
# Repita até que a opção saída seja escolhida (Exercício construído na aula prática 3).

print('Calculadora!')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Digite "s" para finalizar o programa')

while True:
    op = input('Digite qual operação você deseja fazer: ')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('Digite o primeiro número: '))
        y = int(input('Digite o segundo número: '))
        continue
    if op == '+':
        res = x + y
        print('O resultado da adição de {} com {} é de {}.' .format(x,y,res))
        continue
    elif op == '-':
        res = x - y
        print('O resultado da subtração {} com {} é de {}.' .format(x,y,res))
        continue
    elif op == '*':
        res = x * y
        print('O resultado da multiplicação de {} por {} é de {}.' .format(x,y,res))
        continue
    elif op == '/':
        res = x // y
        print('O resultado da divisão {} por {} é de {}.' .format(x,y,res))
        continue
    elif op == "s":
        break
    else:
        print('Operação Inválida!')

print('Encerrando o programa...')