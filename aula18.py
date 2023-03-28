# INTRODUÇÃO AO TRY/EXCEPT

"""
try - Tentar executar o codigo
except - ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar o número que você digitar: ')

try:
    print('STR', numero_str)
    numero_int = int(numero_str)
    print('INT:', numero_int)
    print(f'o dobro de {numero_str} é {numero_int * 2}')
except:
    print('Isso não é um número')