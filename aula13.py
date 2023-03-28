# OPERADORES LÓGICO "AND"

"""
and (e) or (ou) not (não)
and - todas as condições precisam ser verdadeiras
Se qualquer valor for considerado falsy, a expressão inteira sera 
avaliada naquele valor são consideras false.
0 0.0 '' False
Tambem existe o tipo none que é usado para representar um não valor
"""

entrada = input('[E]ntrar ou [S]air? ')
senha_usuario = input('Senha: ')
senha_permitida = '12345'

if (entrada == 'E' or entrada == 'e') and senha_usuario == senha_permitida:
    print('Entrando no sistema . . . ')
else:
    print('Senha incorreta, saindo do sistema . . . ')
