#ESTRUTURA DE REPETIÇÃO WHILE EXECUTA INDETERMINADAS VEZES
opcao = -1

while opcao != 0 :
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
    if opcao == 1:
        print("Sacando....")
    elif opcao == 2:
        print("Exibindo o extrato...")
#UTILIZA ELSE MAS NAO E MUITO UTLIZADO
else:
    print("Obrigado por usar nosso sistema bancario, ate logo!")