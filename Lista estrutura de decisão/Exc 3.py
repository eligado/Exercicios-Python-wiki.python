"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
 F - Feminino, M - Masculino, Sexo Inválido."""

sexo = str(input('Digite o sexo da pessoa "F" - feminino e "M" - masculino: ').upper())

if sexo == 'F':
    print('O sexo e feminino.')
elif sexo == 'M':
    print('O sexo e masculino.')
else:
    print('Sexo inválido.')
