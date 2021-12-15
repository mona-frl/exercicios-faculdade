hotel = ['G','_','*'],['*','_','_']

# cao = 6 --- eq a hotel[1][2]
# queijo = 5 --- eq a hotel [1][1]
# osso = 2 --- eq a hotel [0][1]

# cao - c
# queijo - q
# osso - o

def impr(hotel):
    print('Você venceu!')
    hotel[1][2] = 'C'
    hotel[1][1] = 'Q'
    hotel[0][1] = 'O'
    print(hotel)

for linha in hotel:
    print(linha)

posCao = int(input('Digite a posição para alocar o cão:'))
posQueijo = int(input('Digite a posição para alocar o queijo: '))
posOsso = int(input('Digite a posição para alocar o gato: '))

if posCao == 6 and posQueijo == 5 and posOsso == 2:
    impr(hotel)

else:
    print('Você perdeu! :(')