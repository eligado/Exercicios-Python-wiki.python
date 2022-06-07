# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo.
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

primeiro = int(input('Digite um numero inteiro: '))
segundo = int(input('Digite um numero inteiro: '))
terceiro = float(input('Digite um numero inteiro: '))

A = (primeiro * 2) + (segundo / 2)
B = (primeiro * 3) + terceiro
C = terceiro ** 3

print(f'o produto do dobro do primeiro com metade do segundo é {A}')
print(f'a soma do triplo do primeiro com o terceiro é {B}')
print(f'o terceiro elevado ao cubo é {C}')