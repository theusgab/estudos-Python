# EXERCICIO NUMERO 3

"""
- Crie um programa que faça o usuario digitar a 
senha do banco de dados para obter acesso ao sistema
"""

usuario = input("Nome de Usuario: ")
senha = input("Senha do Usuario: ")

usuario_banco_dados = 'Matheus'
senha_banco_dados = 'Matheus123'

if usuario_banco_dados == usuario and senha_banco_dados == senha:
    print('Conectando...')
else:
    print('Usuario ou senha invalidos')
 