# Lista
cores = ['verde', 'amarelo', 'azul', 'branco']

# Acessando um elemento
print(cores[0])

# Iterando a lista
for cor in cores:
    print(cor)

# Iterando a lista
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

