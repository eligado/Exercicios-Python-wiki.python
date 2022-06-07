# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as
# seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

print('Peso ideal')
sexo = input('Digite H para homem ou M para mulher: ')
altura = float(input('Digite sua altura: '))

if sexo == 'H' or 'h':
    pid = (72.7 * altura) - 58
else:
    pid = (62.1 * altura) - 44.7

print(f'O peso ideal é de {pid}')