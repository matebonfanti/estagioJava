def checa_primo(num):
    for i in range(2, num + 1):
        primo = True
        for j in range(2, int(i ** 0.5) + 1): 
            if i % j == 0:
                primo=False
                
    return primo


def lista_primos(num, p=2):
    if p> num:
        return []
    if checa_primo(p):
        return [p] + lista_primos(num, p + 1) 
    else:
        return lista_primos(num, p + 1)
    

def primosRecursiva():
    print("----------------------------------------------------------------")
    print("------------ Sequencia de Números Primos Recursiva -------------")
    while True:
        num = int(input("Digite o Valor para números primos Recursivo: "))
        if num > 1:
            break
        else:
            print("O número deve ser maior que 1")

    conjunto_primos = lista_primos(num)

    print(conjunto_primos)

    
