# Escreva um algoritmo que leia um valor e que imprima a quantidade de cédulas necessárias para pagar esse mesmo valor.
# Para simplificar, vamos trabalhar apenas com valores inteiros e com cédulas de R$100, R$50, R$20, R$10, R$ 5 e R$1.

valor = int(input('Insira o valor desejado: R$ '))

while True:
    if valor >= 100:
        ced100 = valor // 100
        valor -= ced100 * 100
        print('Cédulas de R$ 100: {}' .format(ced100))
        if not valor:
            break

    if valor >= 50:
        ced50 = valor // 50
        valor -= ced50 * 50
        print('Cédulas de R$ 50: {}' .format(ced50))
        if not valor:
            break

    if valor >= 20:
        ced20 = valor // 20
        valor -= ced20 * 20
        print('Cédulas de R$ 20: {}' .format(ced20))
        if not valor:
            break

    if valor >= 10:
        ced10 = valor // 10
        valor -= ced10 * 10
        print('Cédulas de R$ 10: {}' .format(ced10))
        if not valor:
            break

    if valor >= 5:
        ced5 = valor // 5
        valor -= ced5 * 5
        print('Cédulas de R$ 5: {}' .format(ced5))
        if not valor:
            break

    if valor:
        ced1 = valor
        print('Cédulas de R$ 1: {}'.format(valor))
        break