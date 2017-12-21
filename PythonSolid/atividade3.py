print('Atividade-3 \n Criar um programa que calcule os dados fornecidos pelos usuários \n e diga se ele está apto para entrar no exercito.\n O programa deve conter as seguintes requisitos :\n 1. Deve ser maior de 18 ;\n 2. Deve pesar mais de 60 kg e menos de 90 kg ;\n 3.Deve ter 1.70 Metros de altiura. ')
idade = int(input('Digite aqui sua IDADE'))
peso = float(input('Digite aqui seu PESO'))
altura = float(input('Digite aqui sua ALTURA'))
if idade >= 18 and peso >= 60 and peso <=90 and altura >=1.70:
    print ('Você possui caracteristicas necessarias para ingressar no exercito !')
else:
    print ('Você não possue as Caracteristicas necessarias para ingressar no exercito ')
exit = input ('digite ENTER para finalizar')