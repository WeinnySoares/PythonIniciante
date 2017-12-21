print ("olá mundo")
print (len("olá mundo!"))
# --------------------------------------------------------
# funções
def soma(numero1, numero2):    # <- inicio definição da função
    resp = numero1 + numero2
    return resp                # <- fim definição da função

# soma (11,11)                 chamada da função soma
retorno = soma (11,11)         # <- armazena o valor do retorno em uma variavel 
print (retorno)

# metodo não precisar de retorno.
def imprime_oi():             # <- inicio definição da função
    print("OI")

imprime_oi()                  # <- chamada do método

# valor booleano verdadeiro ou falso para retornar se a função possui 7 letras
def tem_sete_letras(argumento): #<- argumento é o parameto da funsão.
    if len(argumento) == 7:
        return True
    else:
        return False
print("Tem sete letra ? ", tem_sete_letras("vidaloc"))
# print( tem_sete_letras(1234567))  o numero não funciona pois o cada numero é um atributo separado logo não possui len
  
# --------------------------------------------------------
