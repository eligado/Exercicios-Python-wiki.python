# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('Digite uma letra: ').lower())

vogais = 'aeiou'

if letra in vogais:
    print(f'A letra {letra} é uma vogal')
else:
    print(f'A letra {letra} é uma consoante')
