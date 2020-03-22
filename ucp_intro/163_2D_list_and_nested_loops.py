
# 2D list : lista de dos dimenciones
# cada elemento de la primera lista es una lista.
# [] square bracket.

grilla_de_numeros = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]

# primero ponemos el indice de la fila y luego el indice del elemento, de la columna.
print(grilla_de_numeros[0][0]) # para mostrar el numero 1
print(grilla_de_numeros[2][1]) # para mostrar el numero 8


# Bucles anidados For each.
# vamos a recorrer la grilla, primero por fila y luego por columna.

# v1
"""
for fila in grilla_de_numeros:
  print(fila)
"""

# v2
# para cada fila
#  y luego para cada columna de la fila
for fila in grilla_de_numeros:
  for columna in fila:
    print("item: " + str(columna))

