# OPERADORES "IN" E "NOT IN"

"""
Strings são iteràveis
0 1 2 3 4 5 6
M A T H E U S
-7-6-5-4-3-2-1
"""

nome = input('Digite seu nome: ')
encontrar = input('Digite oque deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')


nome = 'Matheus'
print(nome[0], nome[1], nome[2], nome[3], nome[4], nome[5], nome[6] )
print(nome[-7], nome[-6], nome[-5], nome[-4], nome[-3], nome[-2], nome[-1] )

print('theus' in nome) # ESTA ENTRE
