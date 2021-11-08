"""
Tuplas são imutáveis, não podem ter seu conteúdo alterado
    () --> Declaração de tuplas
Listas são mutáveis, podem ter os valores mudados
    [] --> Declaração de lista
"""

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 3, 5, 7, 9
print(tupla2)
print(type(tupla2))

tupla3 = (4)
print(tupla3)
print(type(tupla3))

tupla4 = (4,)
print(tupla4)
print(type(tupla4))

tupla4 = (4,'s')
print(tupla4[1])
print(type(tupla4))

# Desempacotamento
tupla5 = ('Cruso de Python', 'para os melhores professores.')
print(tupla5)
curso, elogio = tupla5
print('1)', curso)
print('2)', elogio)

tupla6 = (1, 2, 3, 4, 5, 6)
print(sum(tupla6))
print(min(tupla6))
print(max(tupla6))
print(len(tupla6))

