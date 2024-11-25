def calculo(numero):
    if numero <= 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return calculo(numero-1) + calculo(numero-2)

def fibonacciRecursiva():

    print("----------------------------------------------------------------")
    print("------------ Sequencia de Fibonacci Recursivo ------------------")
    while True:
        num = int(input("Digite o Valor para o Fibonacci Recursivo: "))
        if num >= 0:
            break
        else:
            print("O número deve ser positivo")

    fib = calculo(num)
    print(f"O Valor de fibonacci de {num} é {fib}.")