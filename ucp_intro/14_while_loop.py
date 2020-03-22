# bucles
"""
La sentencia while o "mientras sea" marca el comienzo de un bucle de repetición.
Los bucles pueden ejecutar el mismo código repetidas veces.
Cuando la ejecución llega hasta una sentencia while, evalúa lacondición junto a la palabra reservada while. Si la condición se evalúa a verdadero (True), la ejecución se
mueve dentro del bloque while Si la condición se evalúa a falso (False), la ejecución se mueve hasta debajo del bloque while.
"""

# while condition :

# Paso & Bandera
i = 1

while i <= 10:
  print(i)
  i += 1 # ojo sino pones esto... nunca se cumple la condición y será un bucle infinito

print("Termine con el bucle")


# Rompiendo el bucle con "break"
# Una sentencia break indica a la ejecución que salga inmediatamente del bucle while y se mueva a la primera línea a continuación del mismo.
