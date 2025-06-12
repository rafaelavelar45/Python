#ESTURTURA DE REPETIÇÃO COM WHILE REPETE QUANTAS VEZES INDETERMINADO
while True:
    numero = int(input("Informe um numero: "))

    if numero == 10:
        break #BREAK CORTA O LAÇO DE UMA EXECUÇÃO



#BREAK TAMBEM UTILIZADO COM FOR

for numero in range (100):

    if numero == 12:
        break #TEM UMA VARIAÇÃO DO BREAK (CONTINUE) ELE PULA UM NUMERO OU ELEMENTO ESPECIFICO NO CASO DESSE NOSSO IF ELE PULA P 12 E CONTINUE CONTANDO ATE 100
    print(numero, end=" ")