
# Que hacemos cuando hay errores en nuestros programas?
# cuando potencialmente tenemos más errores?

# lista completa en https://docs.python.org/3/library/exceptions.html

""" v1
numero = int(input("Ingrese un numero:"))
print(numero)
"""
 #fin v1

# v2 atrapemos ese error potencial
"""

try:
  numero = int(input("Ingrese un numero:"))
  print(numero)
except:
  print("Ingreso invalido")
"""
# ese except asi como esta, capata solo lo que este adentro del try y no otro error en el programa


# v3
# se pueden dar diferentes tipos de errores.

try:
  # value = 10 / 0
  numero = int(input("Ingrese un numero:"))
  print(numero)
except ZeroDivisionError:
  print("Hey! no se puede dividir por 0")
except ValueError:
  print("Ingreso invalido")

#  IndexError("This is an index error")
# para probar un error podes hacer:  raise IndexError("This is an index error")


