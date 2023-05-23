import random

# Definição do intervalo dos números
inicio = 1
fim = 100
quantidade_numeros = 20

# Utilizando a função 'random.sample' para gerar números aleatorios nesse intervalo sem repetições.
numeros_aleatorios = random.sample(range(inicio, fim + 1), quantidade_numeros)
                      
# Encontrar o maior número
maior_numero = numeros_aleatorios[0]
for numero in numeros_aleatorios:
    if numero > maior_numero:
        maior_numero = numero

# Também é possivel utilizar a função 'max' para encontrar o maior número da lista, como no exemplo abaixo: 
# maior_numero = max(numeros_aleatorios)

# Converter os números para Strings
numeros_formatados = [str(num) for num in numeros_aleatorios]

frase = "A lista de 20 números aleatórios gerada foi: "

# Exibindo a lista de números aleatórios, utilizando a função 'join' para retirar os colchetes e adiconar a virgulas entre os números
print(frase, ", ".join(numeros_formatados))
print(f"O maior número da lista é: {maior_numero}")