# COMO O FOR FUNCIONA DEBAIXO DOS PANOS

"""
Iteravel -> str, range, etc
Iterador -> quem sabe entregae um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
"""

texto = 'Matheus'
iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break