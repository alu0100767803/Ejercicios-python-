from romano import *
from entero import *

rom = romano('CMCMCMCM')
rom.romano_a_entero()
print('Valor: ', rom.resultado)

ent = entero(3000)
ent.entero_a_romano()
print('Valor: ', ent.resultado)