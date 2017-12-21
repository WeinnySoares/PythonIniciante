#  range (0, 100, 2) == (valorInicio, valorLimite, valorPular) execulta um loop 
#  for  (variavel) in nomes: (variavel: pode ser qualquer nome que escolher, serve para nomear os itens da lista com um nome generico)
#    print (variavel)
# 'for' é semelhante a instrutura 'para' do algoritmo.
# a função 'len' calcula quantos itens tem na lista.
# While  enquanto é utilisado quando á intenção de reptir uma ação até se atingir um objetivo
# += é uma maneira de especificar que o valor_inicial é somado por ele mesmo e mais o valor_inserido e atribuido ao valor_inicial 
teste = 0
nomes = ['guilherme', 'marcelo', 'joão', 'julia']

for  nome in nomes:
    print (nome)
print('----------------------')

lista_de_numero = range (0, 100, 2)

for item in lista_de_numero:
    print (item)
print('--------------------')

for i in range (len(nomes)):
    print (nomes[i])
    nomes.append('oi') 
print (nomes)

while teste < 10:
    print ('O teste ainda é menor que 10 ', teste)
    teste = teste ++ 1
print('O while acabou :', teste)

print('----------------------')
# essa estrutura é desnecessaria pois a funçãol 'len' já executa o camando de contagem dos valores.
lista_frutas = ['maça','pera', 'uva', 'abacaxi', 'goiaba' ]
contador = 0

for fruta in lista_frutas:
    contador += 1
# fim do contador
print('----------------------')

numero = 0

while True:
    print (numero)
    if numero == 20:
            break
    numero += 1
print ('Saiu do While')