# Dados necessários para classificação: nome e idade
# Classificar qual o ensino para a criança: Ed. Inf. entre 1 a 5 anos; Ed. Fund. I entre 6 e 10 anos; Ed. Fund. II entre
# 11 a 14 anos e Ens. Med. > 15 anos.

while True:  # Utilizei o while para conseguir voltar ao início caso a pessoa queira reiniciar a pesquisa.
    # Dados necessários para o programa rodar:
    nome = input('Digite o nome da criança: ')
    try:  # verificando se o valor informado é inteiro para dar continuidade.
        idade = int(input('Digite a idade da criança: '))  # Idade convertida para número inteiro.
        # verificar se a idade informada é maior ou igual à 1.
        if idade >= 1:
            if idade <= 5:
                print('O(a) aluno(o) {} tem {} anos e está na Educação Infantil.'.format(nome, idade))
            if 10 >= idade >= 6:
                print('O(a) aluno(o) {} tem {} anos e está no Ensino Fundamental I.'.format(nome, idade))
            if 14 >= idade >= 11:
                print('O(a) aluno(o) {} tem {} anos e está no Ensino Fundamental II.'.format(nome, idade))
            if idade >= 15:
                print('O(a) aluno(o) {} tem {} anos e está no Ensino Médio.'.format(nome, idade))
            print('Gostaria de continuar? Pressione 1 para continuar ou pressione qualquer tecla para sair.')
            # Solicitando o valor, ao teclar a pessoa retornará ao início, caso pressione outra tecla o programa
            # fechará.
            decideSeSai = input()
            if decideSeSai == '1':
                continue
            else:
                print('Encerrando o programa...')
                break
        # caso a idade seja 0 retornará a mensagem de idade inválida.
        else:
            print('Idade inválida. Tente Novamente!')
            continue
    except ValueError:
        print('Idade inválida. Tente novamente.')
