cadastro = {}
lista = []

# entrada de dados
while True:

    nome = input('Digite o seu nome: ')
    peso = float(input('Digite o seu peso: '))
    altura = float(input('Digte a sua altura: '))

    cadastro['nome'] = nome
    cadastro['peso'] = peso
    cadastro['altura'] = altura

    lista.append(cadastro.copy())

    # processamento de dados
    IMC = peso / (altura ** 2)

    # saida de dados
    print('{} tem imc {:.2f}.' .format(nome,IMC))

    opcao = int(input('Deseja encerrar o programa? 1 - sim 0 - não\n'))
    if opcao == 1:
        print('Encerrando o programa...')
        break

    print(lista)