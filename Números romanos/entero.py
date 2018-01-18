class entero():
    def __init__(self, numero):
        self.entero = numero
        self.resultado = ''
        
    def entero_a_romano(self):
        if self.entero > 0 and self.entero <= 3000:
            repeticiones = 0
            while self.entero / 1000 != 0:
                repeticiones = int(round((self.entero / 1000)*10)
                self.entero = self.entero % 1000
                for i in repeticiones:
                    self.resultado += 'M'
                    
        else:
            print('Error')