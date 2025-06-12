#IDENTAÇÃO DE BLOCOS EM PYTHON E OBRIGATORIO PARA DEFINIR E DELIMITAR ABERTURA E FECHAMENTO DO BLOCO
def sacar(valor): #abertura de bloco
    saldo = 500
    #quatro espaço para dentro esta dentro do metodo def
    if saldo >= valor:#abertura de bloco
        #quatro espaço para dentro significa que esta dentro do if
        print('Valor sacado!!')
        print('Retira o seu valor na boca do caixa.')
    #fechamento de bloco
    print('Obrigado por ser nosso cliente, tenha um bom dia!') # print está dentro do metodo def
    
#fechamento de bloco

sacar(100)