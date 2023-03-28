# EXERCICIO NUMERO 2

"""
- Faça um programa que peça ao usuario para digitar um numero inteiro.
- Informe se este numero é par ou impar. Caso o usuario não digite um numero inteiro,
informe que não é um numero inteiro.
"""
numero_inteiro = input('Digite um numero: ')

if not numero_inteiro.isdigit():
    print('Isso não é um numero inteiro')
else:
    numero_inteiro = int(numero_inteiro)

    if not numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} é impar')
    else:
        print(f'{numero_inteiro} é par')
