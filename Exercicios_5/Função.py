'''2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo 
(lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True,
responda “Sim”, se o resultado for False, responda “Não”.'''

# Função para verificar se uma palavra ou frase é um palíndromo
def verificar_palindromo(texto):
    # Deixa todas as letras minúsculas para não ter diferença entre maiúsculas e minúsculas
    texto = texto.lower()
    
    # Remove os espaços da frase
    texto = texto.replace(" ", "")
    
    # Verifica se o texto é igual ao seu inverso
    if texto == texto[::-1]:
        return True
    else:
        return False

# Programa principal
print("=== Verificador de Palíndromo ===")

# Pede uma palavra ou frase ao usuário
frase = input("Digite uma palavra ou frase: ")

# Chama a função
resultado = verificar_palindromo(frase)

# Mostra o resultado
if resultado == True:
    print("Sim, é um palíndromo!")
else:
    print("Não, não é um palíndromo.")

  

