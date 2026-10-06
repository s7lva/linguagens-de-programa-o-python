class Pessoa():
    pass

a=Pessoa()
b=Pessoa()
print(a is b) #o is serve para comparar se são o mesmo objeto ou se ambos apontam para o mesmo correto
a=[1,2]
b=[1,2]
print(a is b)
print(a == b)
a=[1]
b=a
print(a is b)
a=[1]
b=a+[] #ou b=a[:]
print(a is b)

# = comparação de id e == compara o que tem dentro o is compara mesma instancia 