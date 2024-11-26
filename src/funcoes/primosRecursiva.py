#Função que verifica se o número é primo, e retorna true ou false
def checa_primo(num):
    for i in range(2, num + 1):
        primo = True
        for j in range(2, int(i ** 0.5) + 1): 
            if i % j == 0:
                primo=False
                
    return primo

#Função recursiva que gera lista de numeros primos até (Num)

def lista_primos(num, p=2):
    #Se o contador for maior que o numero escolhido, retorna vazio
    if p> num:
        return []
    #se for primo, adiciona na lista, chama a função de novo e soma 1 no contador primo
    if checa_primo(p):
        return [p] + lista_primos(num, p + 1)
    #se não for primo, chama a função de novo e soma 1 no contador primo
    else:
        return lista_primos(num, p + 1)
    


#Função chama menu e pede o numero, com validação conforme enunciado
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

    #imrpime o conjunto de numeros primos
    print(conjunto_primos)

    
