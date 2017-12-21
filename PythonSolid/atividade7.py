# EXERCICIO: Escrever um metodo que retorne o maior numero de uma coleção.
# e Escrever um metodo que retorne o menor numero da coleção
colecao = [1,2,3,4,5,6,7] # <- lista

# def NumMaior():
#     for item in colecao:
#         print(item, 'Maior')
def num_maior():
    maior = colecao[0]
    for item in colecao:
        if item > maior:
            maior = item
    print('O maior Valor da coleção é: ',maior)

def num_menor():
    menor = colecao[1]
    for item in colecao:
        if item < menor:
            menor = item
    print('O menor Valor da coleção é: ',menor)
num_maior()
num_menor()