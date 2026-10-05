 

def somarvalores():
    soma = 0
    for x in range(11):
        x = int(input("introduza valores"))
        soma = soma + x
        if x == 0:
            break


    return soma

Soma = somarvalores()

print(f"A soma dos valores são: {Soma}")



   
