# Faça um programa que solicite que o usuário digite um nome. O programa deve imprimir na tela o nome convertido no
# seguinte formato: L*C!@N& Para isso, o programa deve conseguir converter o nome digitado para maiúsculas e
# substituir as vogais pelos símbolos apresentados na tabela abaixo. A = @ E = & I = ! O = # U = *

nome = input('Digite o seu nome: ')
nome = nome.upper()  # converte o 'nome' para letras maiúsculas.
print('{}'.format(nome))  # saída do nome em letras maiúsculas.
print(nome.translate(str.maketrans({'A': '@', 'E': '&', 'I': '!', 'O': '#', 'U': '*'})))  # conversão do texto p/
# caracteres especiais junto com a saída do texto na tela.
print('Finalizando...')
