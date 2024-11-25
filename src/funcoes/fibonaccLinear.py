def fibonacciLinear():
    print("----------------------------------------------------------------")
    print("------------ Sequencia de Fibonacci Linear ---------------------")
    while True:
        num = int(input("Digite o Valor para o Fibonacci Linear: "))
        if num >= 0:
            break
        else:
            print("O número deve ser positivo")