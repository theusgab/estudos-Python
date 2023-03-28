# EXERCICIO 14

"""
Faça um jogo para o usuario advinhar qual
a palavra secreta.
- Voce vai propor uma palavra secreta
qualquer e vai dar a possibilidade para 
o usuario digitar apenas uma letra, voce
vai conferir se a letra digitada 
esta na palavra secreta.
    - Se a letra digitada estiver na palavra
    secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra 
    secreta; exiba *.
Faça a contagem de tentativas do seu usuario.
"""
import os

palavra_secreta = 'apple'
letras_acertadas = ''
numeros_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numeros_tentativas += 1

    if len(letra_digitada) > 1:
        print('Por favor,Digite apenas uma letra!!!')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palavra formada: ', palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU! PARABENS')
        print('A Palavra era', palavra_formada)
        print('Você errou:', numeros_tentativas,'x')
        letras_acertadas = ''
        numeros_tentativas = 0

