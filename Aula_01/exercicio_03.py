"""
Exercício 03
Peça ao usuário para digitar 3 valores inteiros e imprima a soma deles.
"""

print('Digite três números inteiros para somá-los:\n')
num1 = int(float(input('Primeiro número: ').replace(',', '.')))
num2 = int(float(input('Segundo número: ').replace(',', '.')))
num3 = int(float(input('Terceiro número: ').replace(',', '.')))
sum = num1 + num2 + num3
print(f'_____\nA soma dos valores é: {sum}')
