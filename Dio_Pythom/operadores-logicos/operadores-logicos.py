 #OPERADOR E (AND) PARA RETORNAR VERDADEIRO AMBAS TRUE
print(True and True)
print(True and False)
print(False and False)

#OPERADOR OU (OR) PARA RETORNAR VERDADEIRO APENAS UM OU OUTRO RETORNA TRUE
print(True or True)
print(True or False)
print(False or False)

#EXEMPLOS OPERADORES LOGICOS EM EXPRESSAO
saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)
#UTILIZANDO PARANTESES DE ORDEM DE PRECEDENCIA E ORGANIZAÇÃO VISUAL

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

#DICA: NÃO É INTERESSANTE UMA COMPARAÇÃO MUITO LONGA E RECOMENDAVEL QUE QUEBRE POR PARTES E ATRIBUA UMA VARIAVEL