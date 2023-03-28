# EXERCICIO 11

"""
1ª - Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este numero é par ou impar. Caso o usuario não digite um numero
inteiro, informe que não é um numero inteiro.
"""
entrada = input('Digite um numero inteiro: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0 
    par_impar_texto = 'impar' 

    if par_impar:
        par_impar_texto = 'par'

    print(f'O numero {entrada_int} é {par_impar_texto} ')
else:
    print('Você precisa digitar um numero')
    

"""
2ª - Faça um programa que pergunte a hora ao usuario e, baseando-se no horário
descrito, exiba a saudação apropriada. EX.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = input('Digite um horario de 0 a 23 horas:  ')

try:
    horario = int(horario)

    if horario >= 0 and horario <= 12:
        print('Bom dia')
    elif horario >= 12 and horario <= 17:
        print('Boa tarde')
    elif horario >= 18 and horario <= 23:
        print('Boa noite')
except:
    print('Por favor, digite apenas numeros')


"""
3ª - Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é muito curto')
    elif tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Por favor, digite mais de uma letra!')
