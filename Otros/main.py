from Cuenta import *
from Fichero import *

"""cuenta = Cuenta(500)
print("Su saldo: ", cuenta.saldo)
cuenta.retirar(600)
print("Su saldo: ", cuenta.saldo)
cuenta.ingresar(300)
print("Su saldo: ", cuenta.saldo)
cuenta.retirar(100)
print("Su saldo: ", cuenta.saldo)"""

fichero = Fichero(prueba.txt)
print(fichero.leer_fichero())
fichero.mostrar_fichero()