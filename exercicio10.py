# EXERCICIO 10

"""
Peça ao usuario para digitar o seu nome
Peça ao usuario digitar sua idade
Se nome e idade forem digitados:
    Exiba:
    Seu nome é {nome}
    Seu nome Invertido é {nome invertido}
    Se nome contem (ou não) espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}, você tem {idade} anos')
    print(f'Seu nome é invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome CONTÉM espaços ')
    else:
        print('Seu nome NÃO tem espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print("Desculpe você deixou campos vazios.")

