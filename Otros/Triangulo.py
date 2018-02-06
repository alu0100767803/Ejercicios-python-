class Triangulo():
    def __init__(self, anc = 4, car = "*"):
        self.ancho = anc
        self.caracter = car

    def imprimir(self):
        for i in range(1, self.ancho + 1):
            for j in range(i):
                print(self.caracter, end = " ")

            print()

        for i in range(1, self.ancho):
            for j in range(self.ancho - i):
                print(self.caracter, end = " ")
            print()

ancho = int(input("Ancho del triángulo: "))
caracter = input("Caracter del triángulo: ")
triangulo = Triangulo(ancho, caracter)
triangulo.imprimir()
            