# Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário.
# Verifique se os valores formam um triângulo e classifique como:
# a) Equilátero (três lados iguais)
# b) Isósceles (dois lados iguais)
# c) Escaleno (três lados diferentes)

A = int(input('Digite o primeiro lado do triângulo: '))
B = int(input('Digite o segundo lado do triângulo: '))
C = int(input('Digite o terceiro lado do triângulo: '))

if A > 0 and B > 0 and C > 0:
    if A + B > C and A + C > B and B + C > A:
        if A != B and A != C and B != C:
            print('Triângulo escaleno.')
        else:
            if A == B and B == C:
                print('Triângulo equilátero.')
            else:
                print('Triângulo isóscele.')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triângulo.')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo.')