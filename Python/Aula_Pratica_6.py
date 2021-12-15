# Dada uma lista contendo as notas de alunos em uma disciplina, escreva uma expressão para:
import statistics

notas = [9,7,7,10,3,9,6,6,2]

# a) Encontrar quantos alunos tiraram nota 7:
num7 = notas.count(7)
print('Quantidade de alunos que tiraram 7: {}.' .format(num7))

# b) Alterar a última nota para 4:
notas1 = notas[:-1]
notas1.append(4)
print('Alterar a última nota para 4: {}' .format(notas1))

# c) Encontrar a maior nota
maiorNota = max(notas)
print('Maior nota é {}.' .format(maiorNota))

# d) Ordenar a lista de notas
ordem = sorted(notas)
print('Lista de notas ordenada: {}' .format(ordem))

# e) A média das notas
media = statistics.mean(notas)
print('A média das notas é {}.' .format(media))