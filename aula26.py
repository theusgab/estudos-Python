# WHILE / ELSE (Recurso peculiar do Python)

string = 'Valor qualquer'

i = 0 
while i < len(string):
    letra = string[i]

    print(letra)
    i += 1
else:
    print('O else foi executado')
print('Fora do while')

