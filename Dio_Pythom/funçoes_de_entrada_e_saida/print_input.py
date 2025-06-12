#input interagindo com usuario lendo um valor digitado pelo usuario e guardando na variavel nome
nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")
#print exibindo a saida do valor na tela do usuario , no caso o valor informado da variavel nome
print(nome, idade)
#end="\n" quebra de linha em python
print(nome, idade, end="...\n")
#sep="#" utilizando separador
print(nome, idade, sep="#")
#utilizando tanto separado e end no mesmo print
print(nome, idade, sep="#", end="...\n")
