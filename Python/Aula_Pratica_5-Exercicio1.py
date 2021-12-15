# Escreva uma função que calcule o fatorial retorne o seu resultado.
# Faça uma validação dos dados por meio de outra função, permitindo que valores somente positivos sejam aceitos.
# Crie o help da sua função (exercício daapostila aula 5);

def ver_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x


def fatorial(num):
    """
    Calcula a fatorial.
    :param num:
    :return:
    """
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num + 1, 1):
        fat *= i  # fat = fat * i
    return fat


x = ver_int('Digite um valor para calcular a fatorial: ', 0, 99999)
print('{}! = {}'.format(x, fatorial(x)))

