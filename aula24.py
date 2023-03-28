# WHILE + CONTINUE

"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print(f'Numero {contador} OCULTADO')
        continue

    if contador >= 10 and contador <= 27:
        print(f'Numero {contador}, OCULTADO')
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')