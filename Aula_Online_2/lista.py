"""
Listas []
"""

lista1 = [1, 2, 3, 5, 7, 9, 11, 13]
lista2 = ['s', 'e', 'n', 'a', 'c']
lista3 = []
lista4 = list(range(11))
# print(lista4)

# Checando determinador valor contido na lista

num = 9
if num in lista4:
    print(f'Encontrei o múmero {num}')
else:
    print('Não encontrei')

letra = 'e'
if letra in lista2:
    print(f'Encontrei "{letra}" em {lista2}')
else:
    print('Não encontrei')