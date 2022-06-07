# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as
# quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros.
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
# os valores para cima, isto é, considere latas cheias.
import math

metragem = float(input('Entre com a metragem que será pintada(metros quadrados): '))
litros = metragem / 6 * 1.1

# Latas
latas = math.ceil(litros / 18)
valorLata = latas * 80
print(f'Preço para lata(as) de 18 litros R${valorLata}')
print(f'Quantidade de lata(as) usadas {latas}')

# Galões
galao = math.ceil(litros / 3.6)
valorGalao = galao * 25
print(f'Preço para galão(ões) de 3.6 litros R${valorGalao}')
print(f'Quantidade de galão(ões) usadas {galao}')

#misturado
misturalatas = round(litros / 18)
misturagalao = round((litros - misturalatas * 18) / 3.6)
if((litros-(misturalatas*18) % 3.6 != 0)):
    misturagalao += 1
    total = (misturalatas * 80) + (misturagalao * 25)
print(f'Preço para uma compra conjunta entre lata(as) e galão(ões) R${total}')
print(f'Quantidade de  {misturalatas} lata(as) e {misturagalao} galão(ões)')

