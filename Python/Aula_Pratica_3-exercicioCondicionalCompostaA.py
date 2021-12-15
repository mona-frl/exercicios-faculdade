# Se ano é divisível por 4, escreva: “Pode ser um ano bissexto”. Caso contrário, escreva: “Definitivamente não é um
# ano bisexto."
ano = int(input('Digite o ano para consultar: '))

if (ano %4 == 0):
    print('Pode ser bissexto.')
else:
    print('Definitivamente não é bissexto.')