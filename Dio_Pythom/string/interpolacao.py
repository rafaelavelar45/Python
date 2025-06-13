nome = "Guilherme"
idade = 23
profissao = "Programador"
linguagem = "Python"
saldo = 45.435
#Interpolação com % = %s para caractere / %d para numeros inteiros

print("Nome: %s Idade: %d" % (nome, idade))

#Interpolação com  .format , as variaveis tem que vim na ordem que quero preencher  os colchetes

print("Nome: {} Idade: {}".format(nome, idade))

#Interpolação com .format com indice

print("Nome: {0} Idade: {1}".format(nome, idade))

#Interpolação com .format com nomeação

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))

#Interpolação com dicionario

dados = {"nome": "Guilherme", "idade": 28}

print("Nome: {nome} Idade: {idade}".format(**dados))

#Interpolação com F-STRING

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}" ) # SINTAXE :10 significa quantidade de espaço  entre saldo eo valor / .2f quantas casas apos a virugla vai aparecer , o numero de casa voces escolher a quantidade
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}" ) #Neste caso so vai aparecer as casas apos a virgula





