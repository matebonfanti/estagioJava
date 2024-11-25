from funcoes.fibonaccLinear import fibonacciLinear
from funcoes.fibonacciRecursiva import fibonacciRecursiva
from funcoes.primosLinear import primosLinear
from funcoes.primosRecursiva import primosRecursiva

while True:
    print("-------- Bem Vindo  --------------")
    print("----------------------------------------------------------------")
    print("1 - Fibonacci")
    print("2 - Números Primos")
    print("3 - Encerrar")
    n = int(input("Escolha a função desejada: "))
    if n == 1:
        fibonacciLinear()
        fibonacciRecursiva() 
    elif n == 2:
        primosLinear()
        primosRecursiva()
        
    elif n == 3:
        break
    else:
        print("Opção inválida!")



