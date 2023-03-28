# FORMATAÇÃO DE STRINGS

nome = 'Matheus' 
idade = 21 
altura = 1.77 
e_maior = idade > 18 
peso = 77 
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu IMC é de', imc) #tipo 1
print(f'{nome} tem {idade} anos de idade e seu IMC é de {imc:.2f}') #tipo 2
print('{} tem {} anos de idade e seu IMC é de {:.2f}'.format(nome, idade,imc)) #tipo 3