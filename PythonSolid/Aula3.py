#or  ou , and e, not não.
#  Comparações == igual, != não igual, > maior que, < menor que, <= maior ou igual a, >= menor ou igual a.
var_verdade = True
var_falso = False
a = 510
b = 10

if a>b:
    print (a, 'é maior do que',b)
else:
    print(a, 'não é maior do que ', b)
print ('------------------------------------')
print ('-------------Menú-------------------')
opcao = int(input('Para escrever MARIA digite 1 \n Para escrever JOSÉ digite 2 \n Para escrever MARCOS digite 3 \n Para escrever JOÃO digite 4' ))

if  opcao == 1:
    print('Você digitou 1 MARIA')
elif opcao == 2:
    print('Você digitou 2 JOSÉ')
elif opcao == 3:
    print('Você digitou 3 MARCOS')
elif opcao == 4:
    print('Você digitou 4 JOÃO')
else:
    print('Você digitou {} valor é invalido '.format(opcao))
    