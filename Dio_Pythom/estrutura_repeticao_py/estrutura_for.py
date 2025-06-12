#ESTRUTURA DE REPETIÇÃO UTLIZANDO O FOR LITERAVEL

texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'
# for letra = cria uma variagel letra que poderia ser qualquer outro nome , percorre dentro da variavel texto e coloca letra por letra dentro da nossa variavel letra
for letra in texto:
    #letra.upper = deixa todas nossas letrar em MAIUSCULO / in VOGAIS = verifica se a variavel letra contem dentro de vogais
    if letra.upper() in VOGAIS:
        print(letra, end="") #exibe o resultado
#EXECUTA NO FINAL DO LAÇO E NAO É MUITO COMUM NO DIA A DIA
else:
    print() #ADICIONA QUEBRA DE LINHA
    print("Executa no final do laço")