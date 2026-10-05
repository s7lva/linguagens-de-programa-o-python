lista=[]

for x in range(5):
    x = input("introduza os valores na lista")
    lista.append(x)

   
def maiorvalor():
    maior =lista[0]
    for x in lista:
        if x > maior:
            maior = x
    return maior

Maiorvalor = maiorvalor()

print(f"o maior valor é {maiorvalor}")
            

