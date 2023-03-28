# EXERCICIO NUMERO 9

"""
- Criar Input (nome)
- Criar Input (idade)
- criar uma condição de limite de idade para pegar
emprestimo. Com isso saber se o usuario pode ou não
fazer um emprestimo segundo a idade dele.
"""

usuario = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
idade = int(idade)

# Limite para pegar empréstimo
idade_menor = 20 # Muito Jovem
idade_maior = 30 # Passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{usuario} pode pegar o empréstimo')
else: 
    print(f'{usuario} VOCÊ PRECISA SER MAIOR DE IDADE')