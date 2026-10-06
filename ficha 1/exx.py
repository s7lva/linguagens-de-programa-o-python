class Pizza():
    def __init__(self, name, toppings):
        self.__name = name
        self.__toppings = toppings
    
    def toUpper(self):
        return self.__name.upper()
    
    def getName(self):
        return self.__name

    def setName(self, value):
        if len(value)>2:
            self.__name = value


p1 = Pizza("margarita", ["mozzarella", "pommodoro"])

p1.setName("margarida")
p1.setName("m")

p1.setName =( p1.getName + ("extra spicy"))

print (p1.getName()) #OK