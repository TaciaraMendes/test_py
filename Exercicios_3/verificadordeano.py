'''4- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.'''



# Verificador de Ano Bissexto
# Autor: (Seu nome)
# Descrição: Verifica se um ano informado pelo usuário é bissexto ou não.

def eh_bissexto(ano):
    # Regra: é bissexto se for divisível por 4,
    # exceto se for divisível por 100, a menos que também seja por 400.
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False


# Programa principal
print("=== Verificador de Ano Bissexto ===")
try:
    ano = int(input("Digite um ano: "))

    if eh_bissexto(ano):
        print(f"{ano} é um ano bissexto! ✅")
    else:
        print(f"{ano} não é um ano bissexto. ❌")

except ValueError:
    print("Por favor, digite um número inteiro válido para o ano.")
