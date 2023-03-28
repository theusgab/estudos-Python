# FORMATAÇÃO BASICA DE STRINGS

"""
s - srting
d - int
f - float
.<número de digitos>f
x ou X - Hexadecimal
(Caractere) (><^) (quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.4873648123746:0>+10,.1f}')
print('O hexadecimal de 1500 é {1500:08X} ')