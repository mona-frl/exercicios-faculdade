# Implementar um jogo que é popular entre as crianças: um hotel onde os hóspedes têm algumas restrições quanto a
# localização de seu quarto, seguindo as seguintes regras: • O rato não pode ficar ao lado do gato.
# • O cão não pode ficar ao lado do osso. • O gato não pode ficar ao lado do cão. # • O queijo não pode ficar ao lado
# do rato. O jogo é composto por 4 fases, onde cada fase (a partir da fase 2) só é desbloqueada se a anterior for
# concluída com êxito.

hotel = ['I', 'I', 'V', 'G'], ['R', 'V', 'I', 'I']


def hotelprint(hotel):  # quando passar de fase, imprime o código abaixo
    print(' =^.^= Você passou de fase!! =^.^=')
    print()
    for line in hotel:
        print(line)
    print()


def center(str):  # centraliza texto
    str = str.center(50)
    print(str)


def star(str):  # texto bonitinho
    print('*~' * 10, str, '~*' * 10)
    print()


def art():  # desenho do dos quartos/hotel
    print()
    center('        Sejam ')
    print(' ' * 11, ')        bem vindos(as)')
    print(' ' * 9, "( _   _._         ao")
    print(' ' * 10, "|_|-'_~_`-._      Pet Hotel!")
    print(' ' * 7, "_.-'-_~_-~_-~-_`-._")
    print(' ' * 3, "_.-'_~-_~-_-~-_~_~-_~-_`-._")
    print(' ' * 2, '~' * 29)
    print(' ' * 4, '|  [1]   [2]   [3]  [4]  |')
    print(' ' * 4, '|  [5]   [6]   [7]  [8]  |')
    print(' ' * 4, '|                        |')
    print(' ' * 4, '|      <_PetHotel_>      |')
    print(' ' * 4, '|           __           |')
    print(' ' * 2, '._|          | .|          |_._._._._._._._._._._.')
    print(' ' * 2, '|=|________()|__|()________|=|=|=|=|=|=|=|=|=|=|=|')
    print('^^^^^^^^^^^^^^^ ==== ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    print(' ' * 17, '====               Legenda:')
    print(' ' * 19, '====             I - Indisponivel')
    print(' ' * 21, '====           V - Vago')
    print(' ' * 23, '====         C - Cão')
    print(' ' * 25, '====       G - Gato')
    print(' ' * 27, '====     O - Osso')
    print(' ' * 29, '====   Q - Queijo')
    print(' ' * 31, '==== R - Rato')
    print()
    star('Boa sorte!')


def menu():  # menu principal do jogo com os dados para iniciar ou encerrar o jogo.
    star('=^.^= Boa sorte novamente! =^.^=')
    level1()


def loss():  # quando perder — você tem a opção de tentar novamente ou sair do jogo.
    print()
    print('Que pena, você perdeu!')
    print()
    leave = input('Pressione qualquer tecla para tentar novamente ou S para sair do jogo: ')
    if leave == 's' or leave == 'S':
        print('Encerrando o jogo...')
        exit()
    else:
        menu()


def level1():  # 1ª FASE: Gato: 3 e Rato: 6
    star('1ª Fase')
    print('Coloque o gato e o rato em seus quartos:')
    for line in hotel:
        print(line)
    print()
    star('=^.^=')
    posCat = int(input('Digite a posição do gato: '))
    posRat = int(input('Digite a posição do rato: '))

    if posCat == 3 and posRat == 6:
        hotel[0][2] = 'G'
        hotel[1][1] = 'R'
        hotelprint(hotel)
        level2()
    else:
        loss()


def level2():  # 2ª FASE: cão: 7 e 8 e Osso: 1.
    hotel = ['V', 'I', 'I', 'I'], ['I', 'C', 'V', 'V']
    star('2ª Fase')
    print('Coloque os 2 cães e o osso em seus quartos:')
    for line in hotel:
        print(line)
    print()
    star('=^.^= =^.^=')
    posDog1 = int(input('Digite a posição do 1º cão: '))
    posDog2 = int(input('Digite a posição do 2º cão: '))
    posBone = int(input('Digite a posição do osso: '))
    if posDog1 == 7 or posDog1 == 8 and posDog2 == 8 or posDog2 == 7 and posBone == 1:
        hotel[0][0] = 'O'
        hotel[1][2] = 'C'
        hotel[1][3] = 'C'
        hotelprint(hotel)
        level3()
    else:
        loss()


def level3():  # 3.ª FASE: Gato: 7, Rato: 1 e Osso: 5.
    hotel = ['V', 'I', 'I', 'I'], ['V', 'G', 'V', 'I']
    star('3ª Fase')
    print('Coloque o gato, o rato e o osso em seus quartos:')
    for line in hotel:
        print(line)
    print()
    star('=^.^= =^.^= =^.^=')
    posCat = int(input('Digite a posição do gato: '))
    posRat = int(input('Digite a posição do rato: '))
    posBone = int(input('Digite a posição do osso: '))
    if posCat == 7 and posRat == 1 and posBone == 5:
        hotel[0][0] = 'R'
        hotel[1][0] = 'O'
        hotel[1][2] = 'G'
        hotelprint(hotel)
        level4()
    else:
        loss()


def level4():  # 4ª FASE: Queijo: 3 e 1 e Osso: 2.
    print('4ª Fase! ')
    hotel = ['V', 'V', 'V', 'I'], ['I', 'R', 'I', 'I']
    star('3ª Fase')
    print('Coloque os 2 queijos e o osso em seus quartos:')
    for line in hotel:
        print(line)
    print()
    star('=^.^= =^.^= =^.^= =^.^=')
    posCheese1 = int(input('Digite a posição do queijo 1: '))
    posCheese2 = int(input('Digite a posição do queijo 2: '))
    posBone = int(input('Digite a posição do osso: '))
    if posCheese1 == 1 or posCheese1 == 3 and posCheese2 == 1 or posCheese2 == 3 and posBone == 2:
        hotel[0][0] = 'Q'
        hotel[0][2] = 'Q'
        hotel[0][1] = 'O'
        print(' =^.^= Você venceu!! =^.^=')
        print()
        for line in hotel:
            print(line)
        print()
        print()
        leave = input('Pressione qualquer tecla para tentar novamente ou S para sair do jogo: ')
        if leave == 's' or leave == 'S':
            print('Encerrando o jogo...')
            exit()
        else:
            menu()

    else:
        loss()


# codigo principal — como criei tudo em funções o programa é executado a partir da função 'art' que logo em seguida
# aparece o nivel 1 do jogo
art()
print()
level1()
