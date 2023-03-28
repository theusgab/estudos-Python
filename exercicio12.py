# EXERCICIO 12

"""
Iterando strings com while
"""

nome = 'Matheus Gabriel' # Iteráveis

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)