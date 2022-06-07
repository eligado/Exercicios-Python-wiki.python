# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em
# Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input('Qual o tamanho do arquivo em MB? '))
velocidade = float(input('Qual a velocidade da internet em Mbps? '))

tempoFinal = float((tamanho / velocidade) / 60)
print(f'O tempo de download será de {tempoFinal:.2f} minutos.')