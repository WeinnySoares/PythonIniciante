# nas listas e strings o 0 é o primeiro item os pontos : servem para separar aé onde deseja-se visualisar ex: [0:5]
# ao usar o -1 é possível descobrir qual é o ultimo valor da lista ex:[-1:0].
# se necessario pesquisar sobre os atributos de strings do python a diversos.
frase = 'Oi, tudo bem.'
print (frase[0:13])
print (''.join('olá'))

print ('------------------------------------')
lista_nomes = ['João','Maria','Guilherme','Diego']
print (lista_nomes[0:3])
print (lista_nomes[-1:-3])
lista_nomes.append ('Jean') #
print (lista_nomes)
lista_nomes.remove('Jean')
print (lista_nomes)
lista_nomes.insert(0, 'Jair') # insere um nome em determinada posição na lista ex: jair ocup-ara a posição numero 0
print(lista_nomes)
contador = lista_nomes.count('Maria')
print (contador)
print (lista_nomes.pop())
