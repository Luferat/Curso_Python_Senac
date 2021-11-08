carrinho = []
produto = ''

while produto != 'sair':
    produto = input('Adicione o produto na lista ou "sair" para concluir: ')
    if produto != 'sair':
        carrinho.append(produto)

print(carrinho)
