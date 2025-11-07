'''2 - Criar um código que registre as notas de alunos e calcular a média da turma.'''


# Registro de notas e média da turma

print("\n=== Média da Turma ===")

quantidade = int(input("Quantos alunos tem na turma? "))

soma = 0

for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    soma += nota

media = soma / quantidade

print(f"A média da turma é: {media:.2f}")
