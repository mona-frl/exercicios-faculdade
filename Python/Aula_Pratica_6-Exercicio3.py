# Crie um programa para ler o nome, ano de nascimento e sexo de diferentes pessoas. Armazene os dados em um dicionário
# com listas. Ao encerrar o cadastro, apresente: O total de cadastros efetuados; A média das idades das pessoas;
# Uma lista de mulheres com menos de 30 anos; uma lista de homens com idade acima da média.

cadastros = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    terminar = input('Deseja cadastrar uma pessoa? [S/N]\n')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NÃO.')
        continue
    pessoa['nome'] = input('Qual o seu nome?\n- ')
    while True:
        pessoa['sexo'] = input('Qual o seu sexo? [M/F]\n- ').upper()
        if pessoa['sexo'] in 'MF':
            break
        print('Por favor! Apenas digite M ou F.')
    while True:
        try:
            pessoa['ano'] = int(input('Qual ano você nasceu?\n- '))
            break
        except:
            print('Por favor! Digite um ano válido.')

    pessoa['idade'] = 2021 - pessoa['ano']
    soma += pessoa['idade']
    cadastros.append(pessoa.copy())

print(cadastros)
#  O total de cadastros efetuados
print(f'Temos {len(cadastros)} pessoas cadastradas.')
media = soma / len(cadastros)
# A média das idades das pessoas
print(f'A média de idade é de {media:} anos.')
#  Uma lista de mulheres com menos de 30 anos
print('A lista de mulheres com menos de 30 anos são: ', end='')
for mulher in cadastros:
    if mulher['sexo'] == 'F' and mulher['idade'] < 30:
        print(f'{mulher["nome"]}', ' ', end='')
# uma lista de homens com idade acima da média.
print('\nLista dos homens acima da média: ', end='')
for homem in cadastros:
    if homem['idade'] >= media:
        print(f'{homem["nome"]}', ' ', end='')
print('\nPrograma sendo encerrado...')