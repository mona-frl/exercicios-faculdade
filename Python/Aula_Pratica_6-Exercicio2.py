# Crie um jogo de pedra, papel ou tesoura (Jokenpô). Você deverá jogar contra o computador. Você irá sempre escolher uma
# das opções: 1 pedra, 2 papel, 3 tesoura

import random


def ver_int(pergunta, min, max):  # verificar dados da pergunta.
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x


def vencedor(jogador1, jogador2):
    global empate, v1, v2
    if jogador1 == 1:  # pedra
        if jogador2 == 1:  # pedra
            empate += 1
        elif jogador2 == 2:  # papel
            v2 += 1
        elif jogador2 == 3:  # tesoura
            v1 += 1

    if jogador1 == 2:  # papel
        if jogador2 == 1:  # pedra
            v1 += 1
        elif jogador2 == 2:  # papel
            empate += 1
        elif jogador2 == 3:  # tesoura
            v2 += 1

    if jogador1 == 3:  # tesoura
        if jogador2 == 1:  # pedra
            v2 += 1
        elif jogador2 == 2:  # papel
            v1 += 1
        elif jogador2 == 3:  # tesoura
            empate += 1
    resultados = [v1, v2, empate]
    return resultados


# Programa Principal
print('JOKENPO')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

resultados = []
jogadas = []
v1 = 0
v2 = 0
empate = 0

while True:
    jogador1 = ver_int('Escolha sua jogada: ', 0, 3)
    if not jogador1:
        break
    jogador2 = random.randint(1, 3)
    jogadas.append((jogador1, jogador2))
    resultados = vencedor(jogador1,jogador2)

    for jogada in jogadas:
        for dado in jogada:
            print(dado, end=' ')
        print()

print('Numedo de vitórias do jogador 1: {}' .format(resultados[0]))
print('Numedo de vitórias do jogador 2: {}' .format(resultados[1]))
print('Numedo de empates: {}' .format(resultados[3]))
