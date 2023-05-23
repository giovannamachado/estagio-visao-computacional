import pandas as pd 

#Utilizei a biblioteca 'pandas' para abrir e ler o arquivo csv 
tabela = pd.read_csv("numeros.csv", header=None) 

soma = 0

# Convertir os dados para lista
numeros = tabela.values.flatten().tolist()

# Usei o for para peccorrer cada número e o if para verificar se é um numero impar
for num in numeros:
    if num % 2 != 0:
        soma += num
  

print(f'A soma dos números ímpares é: {soma}')

        