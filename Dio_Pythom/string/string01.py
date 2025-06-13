nome = "rAfaEL"
#DEIXA A STRING MAIUSCULA
print(nome.upper())
#DEIXA A STRING minuscula
print(nome.lower())
#DEIXA A STRING COMO TITULO PRIMEIRA LETRA MAIUSCULA 
print(nome.title())

#ELIMINANDO OS ESPAÇOS EM BRANCO

texto = "   Olá, Mundo!  "
print(texto + ".")
#TIRA OS ESPAÇOS DE AMBOS OS LADOS DO TEXTO
print(texto.strip() + ".")
#TIRA OS ESPAÇOS DA ESQUERDA
print(texto.rstrip() + ".")
#TIRA OS ESPAÇOS DA DIREITA
print(texto.lstrip() + ".")

#JUNÇÕES E CENTRALIZAÇÕES

menu = "Python"

print("####" + menu + "####") 

print(menu.center(14, "#")) # Centraliza a variavel ao meio conforme a qautidade de espaços definidas automaticamente tem o parametro para colocar simbolo  .center

#JUNÇÕES

print("P-y-t-h-o-n")
print("-".join("Python")) #faz a junção com .Join