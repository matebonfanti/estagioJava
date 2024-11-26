#Função que mostra menu, pede numero desejado e valida conforme enunciado
def primosLinear():
    print("----------------------------------------------------------------")
    print("------------ Sequencia de Números Primos Linear ----------------")
    while True:
        num = int(input("Digite o Valor para números primos Linear: "))
        
        if num > 1:
            break
        
        else:
            print("O número deve ser maior que 1")
    #Cria Conjunto vazio        
    conjunto = []
    #For para verificar se numero é primo, se for adiciona na lista 
    for i in range(2, num + 1):
        primo = True
        for j in range(2, int(i ** 0.5) + 1): 
            if i % j == 0:
                primo=False
                break
        if primo:
            conjunto.append(i)


    #Mostra Lista
    print(conjunto)