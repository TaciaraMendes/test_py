# Verificação de senha

print("\n=== Verificação de Senha ===")

senha = input("Digite uma senha: ")

# Verifica se tem pelo menos 8 caracteres
tem_tamanho = len(senha) >= 8

# Verifica se tem algum número
tem_numero = False
for caractere in senha:
    if caractere.isdigit():
        tem_numero = True
        break

# Mostra resultado
if tem_tamanho and tem_numero:
    print("Senha válida!")
else:
    print("Senha inválida! A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")


