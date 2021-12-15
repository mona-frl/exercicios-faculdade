# Realize a sequência de print com for e while
# a) Inteiros de 3 até 12, com 12 incluso
# b) Inteiros de 0 até 9, excluindo 9, com passo de 2 while x for

# A
for x in range(3, 13, 1):
    print(x)

#

x = 3

while x < 13:
    print(x)
    x += 1

# B

x = 0

while x < 9:
    print(x)
    x += 2

#

for x in range(0, 9, 2):
    print(x)
