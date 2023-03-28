# INSERINDO ITENS

"""
Listas em python
Tipo list - Mutavel
Suporta vários valores de qualquer tipo 
Conhecimentos reutilizaveis - Indices e fatiamento
Métodos uteis:
    .append - Adiciona um item ao final  
    .insert - Adiciona um item no indice escolhido
    .pop - Remove do final ou do indice escolhido
    .del - Apaga um indice
    clear - Limpa a lista
    extend - Estende a lista
    + - Concatena listas
"""

#        0    1   2   3
lista = [10, 20, 30, 40]
lista.append('Matheus')
nome = lista.pop()      
lista.append(1233)      
del lista[-1]   
lista.insert(0, 5)        
print(lista[5])