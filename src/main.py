#import das funções
from funcoes.fibonaccLinear import fibonacciLinear
from funcoes.fibonacciRecursiva import fibonacciRecursiva
from funcoes.primosLinear import primosLinear
from funcoes.primosRecursiva import primosRecursiva

#Menu que fica em loop até encerrar
while True:
    print("----------------------- Bem Vindo  -----------------------------")
    print("----------------------------------------------------------------")
    print("1 - Fibonacci")
    print("2 - Números Primos")
    print("3 - Encerrar")
    n = int(input("Escolha a função desejada: "))

    #Chamada das funções conforme a escolha do usuário
    if n == 1:
        fibonacciLinear()
        fibonacciRecursiva() 
    elif n == 2:
        primosLinear()
        primosRecursiva()
     #Opção 3 sai do loop e encerra   
    elif n == 3:
        break
    #Caso a opção escolhida seja inválida, exibe a mensagem de erro
    else:
        print("Opção inválida!")



