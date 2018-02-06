class Cuenta():
    def __init__(self, cantidad = 0):
        self.saldo = cantidad
    
    def ingresar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if self.saldo - cantidad > 0:
            self.saldo -= cantidad
        else:
            print('Operación cancelada: No dispone de ', cantidad, ' en su cuenta')
            