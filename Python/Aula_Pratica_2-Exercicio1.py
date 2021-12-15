# Desenvolva um algoritmo que solicite ao usuário o preço de um produto, um percentual de desconto a ser aplicado a ele.
# Calcule e exiba o valor do desconto e o preço final do produto.

preco = float(input('Digite o preço do produto: '))
percentual = float(input('Digite o percentual de desconto (0-100): '))

desconto = preco * (percentual / 100)
final = preco - desconto

print('O preço final do produto é de {}. O desconto será de {}%.'.format(preco, percentual))
print('O valor calculado de desconto é de: {} sendo o valor final do produto:{}.'.format(desconto, final))
