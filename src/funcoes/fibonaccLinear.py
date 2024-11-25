def fibonacciLinear():
    print("----------------------------------------------------------------")
    print("------------ Sequencia de Fibonacci Linear ---------------------")
    while True:
        num = int(input("Digite o Valor para o Fibonacci Linear: "))
        if num >= 0:
            break
        else:
            print("O número deve ser positivo")

    if num <= 0: 
        print("0") 
    elif num == 1: 
        print("1")
        
   
    f1 = 0
    f2 = 1

    for i in range(2, num + 1):
        f1, f2 = f2, f1 + f2
    print(f"O Valor de fibonacci de {num} é {f2}.")

    
