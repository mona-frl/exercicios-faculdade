# Uma escola de cursos de TI, oferece vouchers para que os par-ticipantes possam assistir algumas aulas gratuitas de
# Python. Para isso o participante que deseja assistir às aulas gratuitas desse curso específico, deve fazer uma
# inscrição para receber o voucher. Implemente um programa que armazene as inscrições para o curso.
# O programa deverá armazenar para cada inscrição: um código único para o voucher; Nome; Email;Telefone,; Curso.
# O programa deverá apresentar um menu de opções ao usuário: 1 — inscrição 2 — visualizar inscrição 0 — Encerrar.

from random import randint

cadastros = list()
pessoa = dict()
voucher = 0

while True:
    print("|", '-' * 15, 'MENU', '-' * 15, "|")  # print do me-nu para seleção
    print("|", ' ' * 1, 'Selecione uma das opções abaixo:', ' ', "|")
    print("|", ' ' * 5, ' 1 - Inscrição', ' ' * 15, "|")
    print("|", ' ' * 5, ' 2 - Visualizar Inscrição', ' ' * 4, "|")
    print("|", ' ' * 5, ' 0 - Encerrar', ' ' * 16, "|")
    print("|", '-' * 36, "|")

    try:
        op = int(input('Digite a opção selecionada: '))

        if op == 1:  # Fará o cadastro do usuário
            pessoa.clear()
            print('Opção selecionada: 1 - Inscrição.')
            print("|", '-' * 36, "|")
            pessoa['nome'] = input('Nome completo: ')
            pessoa['email'] = input('Digite seu e-mail: ')
            while True:
                try:  # se o número não for inteiro ou válido, dará erro gerado no except
                    pessoa['telefone'] = int(input('Digite o número do seu telefone celular: '))
                    break
                except:
                    print('Por favor, digite um número váli-do!')
            pessoa['curso'] = input('Digite seu curso: ')
            voucher = randint(1000,9999)  # gerando o voucher
            cadastros.append(pessoa.copy())  # adicionando os dados no dicionário de cadastros e na lista de pessoa.
            print('Cadastro efetuado com sucesso!\n')
            print('Confira sua inscrição na opção 2 do menu.')
            print("|", '-' * 36, "|",'\n\n')

        elif op == 2:  # Mostrará a inscrição feita.
            while True:
                try:
                    print('Opção selecionada: 2 - Visualizar Inscrição.\n\n')
                    print("|", '-' * 36, "|")
                    print('Nome: {}'.format(pessoa['nome']))
                    print('E-mail: {}'.format(pessoa['email']))
                    print('Telefone: {}'.format(pessoa['telefone']))
                    print('Curso: {}'.format(pessoa['curso']))
                    print('O número do seu voucher é: {}'.format(voucher))
                    print("|", '-' * 36, "|",'\n\n')
                except:
                    print('Por favor, faça seu cadastro primei-ramente!')
                    print("|", '-' * 36, "|", '\n\n')
                    break

        elif op == 0:
            print('Encerrando programa...')
            print('Programa encerrado com sucesso!')
            break
    except:
        print('Opção inválida!\n Por favor, selecione uma opção do menu...\n')
