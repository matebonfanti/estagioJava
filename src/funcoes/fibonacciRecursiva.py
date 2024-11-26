#Função de fibonacci recursiva, verifica 0 e 1, se nao retorna chamadando a função novamente
def calculo(numero):
    if numero <= 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return calculo(numero-1) + calculo(numero-2)

#Menu com validação conforme enunciiado
def fibonacciRecursiva():

    print("----------------------------------------------------------------")
    print("------------ Sequencia de Fibonacci Recursivo ------------------")
    while True:
        num = int(input("Digite o Valor para o Fibonacci Recursivo: "))
        if num >= 0:
            break
        else:
            print("O número deve ser positivo")
    #chama a função de fibonacci recursiva e salva resultado em 'fib'
    fib = calculo(num)
    #Mostra resultado
    print(f"O Valor de fibonacci de {num} é {fib}.")