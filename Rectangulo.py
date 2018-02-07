class Rectangulo():
    def __init__(self, alt = 5, anc = 10, car = "*"):
        self.alto = alt
        self.ancho = anc
        self.caracter = car

    def imprimir(self):
        for i in range(self.alto):
            for j in range(self.ancho):
                print(self.caracter, end=" ")
            print()
            

alto =  int(input("Alto del rectángulo: "))
ancho = int(input("Ancho del rectángulo: "))
caracter =  input("Caracter del rectángulo: ")
rectangulo = Rectangulo(alto, ancho, caracter)
rectangulo.imprimir()