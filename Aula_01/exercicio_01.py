"""
Exercício 01
Faça um programa que leia um número inteiro e o imprima.
"""

num = input('Digite um número inteiro: ')
num = int(float(num.replace(',', '.')))
print(f'O número digitado foi {num}')
