# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
# preço total.
import math

metragem = float(input('Entre com a metragem que será pintada(metros quadrados): '))
litros = metragem / 3

latas = math.ceil(litros / 18)
valorLata = latas * 80
print(f'Preço para lata(as) de 18 litros R${valorLata}')
print(f'Quantidade de lata(as) usadas {latas}')