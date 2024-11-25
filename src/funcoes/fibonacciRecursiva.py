def fibonacciRecursiva():
    print("----------------------------------------------------------------")
    print("------------ Sequencia de Fibonacci Recursivo ------------------")
    while True:
        num = int(input("Digite o Valor para o Fibonacci Recursivo: "))
        if num >= 0:
            break
        else:
            print("O número deve ser positivo")