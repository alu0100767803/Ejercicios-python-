class Fichero():
    def __init__(self, ruta_fichero):
        self.ruta = ruta_fichero
        self.texto = ''

    def leer_fichero(self):
        try:
            self.text = open(self.ruta).read()
        except IOError:
            print('ERROR: nose puede abrir el fichero ', self.ruta)
        return self.texto
    
    def mostrar_fichero(self):
        print (self.texto)