
def maiorvalor():
    lista =[1,2,3,5,4]
    maior = lista[0]
    for x in lista:
        if x > maior:
            maior = x

    return maior

print(f"maior valor é  {maiorvalor()}")
