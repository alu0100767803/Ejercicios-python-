class romano():
    def __init__(self, numero):
        self.romano = numero
        self.resultado = 0
        self.valores = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

    def romano_a_entero(self):
        anterior = 0                    # Valor del número romano anterior en decimales
        actual = 0                      # Valor del número romano actual en decimales
        repeticiones = 0                # Número de repeticiones seguidas de una letra
        l_repeticiones = ''
        l_actual = ''                   # Letra del número romano actual
        l_anterior = ''                 # Letra del número romano anterior

        if len(self.romano) > 0:
            anterior = self.valores[self.romano[0]]
            l_anterior = self.romano[0]
        
        for letra in self.romano:
            if letra in self.valores:
                actual = self.valores[letra]
                l_actual = letra
            else:
                print('Valor incorrecto:', letra)
                resultado = 'NaN'

            if anterior > actual:
                self.resultado += actual

            elif anterior == actual:
                l_repeticiones = l_actual
                repeticiones += 1
            
            else:
                if l_anterior == 'C' and (l_actual == 'M' or l_actual == 'D') or l_anterior == 'X' and (l_actual == 'C' or l_actual == 'L') or l_anterior == 'I' and (l_actual == 'V' or l_actual == 'X'): 
                    aux = actual - 2 * anterior
                    self.resultado += aux
                    if l_repeticiones == l_actual:
                        repeticiones += 1

                else:
                    print('Valor incorrecto:', l_anterior,l_actual)
                    self.resultado = 'NaN'
                    break
                    

            anterior = actual
            l_anterior = l_actual

            if repeticiones > 3:
                print('Valor incorrecto: hay mas de 3 repetciones de', l_actual)
                self.resultado = 'NaN'
                break
