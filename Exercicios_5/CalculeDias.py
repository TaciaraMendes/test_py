'''4 - Crie um programa que calcule a quantos dias
um individuo está vivo de acordo com a data do dia.'''

# Importa a biblioteca datetime, que trabalha com datas
from datetime import date

# Programa principal
print("=== Calculadora de Dias de Vida ===")

# Pede o ano, mês e dia de nascimento do usuário
ano = int(input("Digite o ano do seu nascimento (ex: 2000): "))
mes = int(input("Digite o mês do seu nascimento (ex: 5 para maio): "))
dia = int(input("Digite o dia do seu nascimento: "))

# Cria uma data de nascimento com as informações do usuário
data_nascimento = date(ano, mes, dia)

# Pega a data de hoje automaticamente
data_atual = date.today()

# Calcula a diferença entre a data atual e a data de nascimento
dias_de_vida = (data_atual - data_nascimento).days

# Mostra o resultado
print("Você está vivo há", dias_de_vida, "dias!")
