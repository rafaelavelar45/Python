
#Estrutura condicional if ternario permite escrever uma condição em uma unica linha
saldo = 2000
saque = 2500

status = 'Sucesso' if saldo >= saque else 'Falha'

print(f"{status} ao realizar o saque!")