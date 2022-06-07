# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nome = input('Digite o nome do aluno: ')
primeiro_bimestre = float(input('Digite a do primeiro bimestre: '))
segundo_bimestre = float(input('Digite a do primeiro bimestre: '))
terceiro_bimestre = float(input('Digite a do primeiro bimestre: '))
quarto_bimestre = float(input('Digite a do primeiro bimestre: '))

media_final = (primeiro_bimestre + segundo_bimestre + terceiro_bimestre + quarto_bimestre) / 4

print(f'A média do {nome} é de {media_final}.')
