"""
Exercício 09
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
A fórmula de conversão é: K =  C + 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.
"""

tempC = float(input('Digite a temperatura em Celsius: ').replace(',', '.'))
tempK = tempC + 273.15
print(f'{tempC}°C = {tempK}°K')
