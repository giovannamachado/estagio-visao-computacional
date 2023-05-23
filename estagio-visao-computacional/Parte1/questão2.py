
#Função criada para veficiar se é um palidromo e transforma as letras das palavras todas em minúsculas.
def palindromo(palavra):
   palavra = palavra.lower()
   return palavra == palavra[::-1]


palavra_dada= input("Digite a palavra para verificação: ")
verificacao = palindromo(palavra_dada)

if verificacao:
   print(f"Sim, a palavra {palavra_dada} é palíndroma")
else:
   print(f"Não, a palavra {palavra_dada} não é palíndroma",)