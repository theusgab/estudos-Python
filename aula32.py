# ESCOPO DE VARIAVEIS

"""
Variaveis Globais / são decladas FORA de todos o blocos de funções

Variaveis Locais / são declaradas DENTRO do bloco de funções
"""

x = 5

def funcao():
    x = 3
    print('Valor da variavel local: ', x)

funcao()
print('Valor da variavel global ', x)

nome = 'Gabriel'
altura = 1.74
cpf = '000.000.000.00'
idade = 23