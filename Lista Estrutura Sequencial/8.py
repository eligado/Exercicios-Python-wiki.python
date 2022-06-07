# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
salarioHr = float(input('Digite o quanto você ganha por hora: '))
hrTrabalhada = int(input('Digite quantas horas foram trabalhadas no mês: '))

salarioMs = (salarioHr * hrTrabalhada)

print(f'O salário do mês será de ${salarioMs}')