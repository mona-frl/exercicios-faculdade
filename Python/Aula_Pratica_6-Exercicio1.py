# Escreva um algoritmo que crie uma tupla com 10 palavras. Encontre dentro dessa tupla as vogais de cada palavra. Faça
# um print na tela com o nome da palavra e suas respectivas vogais.

palavras = ('Monalisa', 'Patrick', 'Edelcio', 'Junior', 'Fabricio', 'Cleusa', 'Gerda', 'Gisele', 'Geke', 'Lianne')

for palavra in palavras:
    print('\nNome: {}  \nVogais:  ' .format(palavra.upper()))
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
