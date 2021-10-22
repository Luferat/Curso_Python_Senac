"""
Exercício 07
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = 5.0 * (F - 32.0)/9, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.
"""

tempF = float(input('Digite a temperatura em Fahrenheit: ').replace(',', '.'))
tempC = 5 * (tempF - 32)/9
print(f'{tempF}ºF = {tempC}ºC')
