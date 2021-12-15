# Suponha que você é um colecionar de jogos de videogame. Escreva um algoritmo que permita cadastrar esses jogos
# informando o nome e a qual videogame ele pertence. Para isso, crie um menu de opções contendo:
# cadastrar novo “item”, listar tudo que foi cadastrado e sair.

def ver_int(pergunta, min, max):  # verificar dados da pergunta.
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x


def makeFile(nomeArquivo):  # criar um arquivo quando inexistente
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação de arquivo.')
    else:
        print('Arquivo {} criado com sucesso!\n'.format(nomeArquivo))


def verFile(nomeArquivo):  # verificar se existe o arquivo
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def listarFile(nomeArquivo):  # listar os jogos cadastrados
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler arquivo...')
    else:
        print(a.read())
    finally:
        a.close()


def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideoGame):  # cadastrar o jogo
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        a.write('{};{}\n'.format(nomeJogo, nomeVideoGame))
    finally:
        a.close()


# Programa Principal
arquivo = 'games.txt'
if verFile(arquivo):
    print('Arquivo localizado no computador.')
else:
    print('Arquivo inexistente... \nCriando arquivo...\n')
    makeFile(arquivo)

while True:
    print('MENU')
    print(' 1 - Cadastrar um novo item')
    print(' 2 - Listar cadastros')
    print(' 3 - Sair')

    op = ver_int('Escolha a opção desejada: ', 1, 3)
    if op == 1:
        print('Cadastro de novo item selecinado...\n')
        nomeJogo = input('Coloque o nome do jogo: ')
        nomeVideoGame = input('Coloque o nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideoGame)
    elif op == 2:
        print('Lista de todos os itens selecinada...\n')
        listarFile(arquivo)
    elif op == 3:
        print('Encerrando o programa...')
        break
