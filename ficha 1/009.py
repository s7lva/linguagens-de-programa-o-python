import math

" cria a classe Pizzas que representa todas e "
"tem como argumentos nome a lista dos ingredientes e o tamanho de cada um"
class Pizzas():
    diametro_cm = 30
    def __init__(self, nome , tamanho , ingredientes):
        """
        param: nome : o nome da pessoa
        param: idade: idade da pessoa
        """
        self.nome = nome
        self.tamanho = tamanho
        self.ingredientes = ingredientes

        if ingredientes is None:
            self.ingredientes = ["tomate", "queijo mozarella"]
        else:
            self.ingredientes = ingredientes


    "calcular a area da pizza media que foi defenida como 30cm"
    @classmethod
    def calcular_area(cls):
      area =  math.pi * math.pow(cls.diametro_cm /2 ,2) #função de calcular a area
      return area 

    def calcular_peso(self):
           total =0
           for ingrediente in self.ingredientes:
               total += ingrediente.peso

           return total

"classe dos ingredientes ligada a classe pizza onde os ingredientes passam a ter nome e pessos"
"e os mesmos vão para a classe Pizza e para a lista ingredientes ."
class Ingredientes():
    def __init__ (self,gramas, nomeingredientes ):
      """
      param: nomeingredientes = nome do ingrediente das pizzas
      param: peso: A medida em gramas ou quantidade dos ingredientes 
      """
      self.nomeingredientes = nomeingredientes
      self.peso = gramas

    


pizza1 = Pizzas(
    "margarita",
    10,
    [
        Ingredientes(200, "tomate"),
        Ingredientes(100, "cogumelos"),
        Ingredientes(300, "Frango"),
    ]
)


print(pizza1.nome.upper())
print("Area do circulo " , pizza1.calcular_area() , "m^2")
print("Pesso total : " , pizza1.calcular_peso(), "g")


